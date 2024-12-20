
const mapStyles = {
    default: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    dark: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png',
    satellite: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    topo: 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'
};

const NUCLEAR_EFFECTS = {
    FIREBALL: { color: '#ff0000', opacity: 0.1, order: 1, addedDuration: 0 },
    SEVERE_BLAST: { color: '#ff4500', opacity: 0.1, order: 2, addedDuration: 200 },
    MODERATE_BLAST: { color: '#ffa500', opacity: 0.1, order: 3, addedDuration: 400 },
    THERMAL: { color: '#ffff00', opacity: 0.1, order: 4, addedDuration: 500 },
    RADIATION: { color: '#9932cc', opacity: 0.1, order: 5, addedDuration: 700 },
    FALLOUT: { color: '#00ff00', opacity: 0.1, order: 6, addedDuration: 1000 }
};

const canvas = document.createElement('canvas');
canvas.style.position = 'fixed';
canvas.style.top = '0';
canvas.style.left = '0';
canvas.style.width = '100%';
canvas.style.height = '100%';
canvas.style.pointerEvents = 'none';
canvas.style.zIndex = '9997';
document.body.appendChild(canvas);

const ctx = canvas.getContext('2d');

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function createVHSEffect() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Random color offset
    if (Math.random() > 0.95) {
        ctx.fillStyle = `rgba(255, 0, 0, ${Math.random() * 0.1})`;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }

    // Tracking lines
    for (let i = 0; i < canvas.height; i += 2) {
        if (Math.random() > 0.99) {
            ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
            ctx.fillRect(0, i, canvas.width, 1);
        }
    }

    // Glitch effect
    if (Math.random() > 0.95) {
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const w = Math.random() * 100;
        const h = Math.random() * 100;
        ctx.drawImage(canvas, x, y, w, h, x + Math.random() * 10 - 5, y, w, h);
    }

    requestAnimationFrame(createVHSEffect);
}

createVHSEffect();

function calculateAtomicBombRadiusInMetersWithKilotons(kilotons) {
    return 0.1 * Math.cbrt(kilotons) * 1000;
}

function calculateEffectRadius(kilotons, effect) {
    switch(effect) {
        case 'FIREBALL':
            return Math.pow(kilotons, 0.4) * 100; // Fireball radius
        case 'SEVERE_BLAST':
            return Math.pow(kilotons, 0.5) * 300; // Severe damage
        case 'MODERATE_BLAST':
            return Math.pow(kilotons, 0.5) * 600; // Moderate damage
        case 'THERMAL':
            return Math.pow(kilotons, 0.5) * 1200; // Thermal effects
        case 'RADIATION':
            return Math.pow(kilotons, 0.5) * 1500; // Initial radiation
        case 'FALLOUT':
            return Math.pow(kilotons, 0.5) * 2000; // Fallout initial
    }
}

let circle;
let circles = {};
//http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
let city = document.getElementById('place').value;

async function getCoordsFromCity(city) {
    if (!city) {
        city = "Helsinki";
    }
    const cityResponse = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=c54b18aed750b9677d90d64c0669c411`);
    const cityData = await cityResponse.json();
    return [cityData[0].lat, cityData[0].lon];
}

async function getCoords() {
    const city = document.getElementById('place').value;
    const csa = await getCoordsFromCity(city);
    return csa;
}
async function getPopulationDensity(lat, lon, radius) {
    try {
        // GeoNames API with username (you need to register at geonames.org)
        const GEONAMES_USERNAME = 'aatu'; // Replace with your username
        const radiusKm = radius / 1000;

        const response = await fetch(
            `http://api.geonames.org/findNearbyPlaceNameJSON?` +
            `lat=${lat}&lng=${lon}&radius=${radiusKm}&maxRows=10&username=${GEONAMES_USERNAME}`
        );

        const data = await response.json();

        if (!data.geonames || data.geonames.length === 0) {
            throw new Error('No population data found');
        }

        // Calculate total population in radius
        let totalPopulation = data.geonames.reduce((sum, place) => {
            return sum + (parseInt(place.population) || 0);
        }, 0);

        // Calculate area in km²
        const areaKm2 = Math.PI * Math.pow(radiusKm, 2);

        // Adjust population based on radius overlap
        const adjustedPopulation = Math.round(totalPopulation * (radiusKm / 10));
        const density = Math.round(adjustedPopulation / areaKm2);

        return {
            population: adjustedPopulation,
            density: density,
            area: Math.round(areaKm2)
        };
    } catch (error) {
        console.error('Population data error:', error);
        document.getElementById('error').innerHTML = 'Could not fetch population data';
        return null;
    }
}

// const themeaudio = new Audio('assets/themesong.wav');
// themeaudio.loop = true;
// themeaudio.play();

// if mouse  clicked add sound
document.addEventListener('click', function () {
    const audio = new Audio('assets/piip' + Math.floor(Math.random() * 8 + 1) + '.wav');
    audio.play();
});

document.addEventListener('keydown', function (event) {
    const audio = new Audio('assets/key' + Math.floor(Math.random() * 2 + 1) + '.wav');
    audio.play();
});

document.getElementById('didyouknow').addEventListener('click', function () {
    var randfact = "";
    fetch("http://localhost:1234/random")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        randfact = data.fact;
        document.getElementById('rah').innerHTML = randfact;
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
});


document.addEventListener("DOMContentLoaded", async function () {
    // MUSIC


    const themeButton = document.getElementById('playTheme');
    const themeSound = document.getElementById('themeSound');

    themeButton.addEventListener('click', async () => {
        // muet
        if (themeSound.paused) {
            themeSound.play();
            themeButton.textContent = '🔇 Mute Theme';
        } else {
            themeSound.pause();
            themeButton.textContent = '🎵 Play Theme';
        }
    });

    document.getElementById('place').value = "Helsinki";
    const csa = await getCoords();
    const map = L.map('map').setView(csa, 13);

    let currentLayer = L.tileLayer(mapStyles[document.getElementById('mapStyle').value], {
        maxZoom: 19,
    }).addTo(map);

    document.getElementById('mapStyle').addEventListener('change', function () {
        map.removeLayer(currentLayer);
        currentLayer = L.tileLayer(mapStyles[this.value], {
            maxZoom: 19,
        }).addTo(map);
    });

    marker = L.marker([11160.1695, 21114.9354]).addTo(map);

    // Initial circle

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            document.getElementById('calculateBtn').click();
        }
    });

    function easeOutCirc(x) {
        return Math.sqrt(1 - Math.pow(x - 1, 2));
    }

    // Add click event listener to button
    document.getElementById('calculateBtn').addEventListener('click', async function () {
        const audio = new Audio('assets/PSUUUUUUUUUUUUUUUUUUUUUUUSHSH.wav');
        audio.play();
        
        const kilotons = document.getElementById('kilotons').value;
        const csa = await getCoordsFromCity(document.getElementById('place').value);
        
        // Update map view and marker
        map.setView(csa, 13);
        marker.setLatLng(csa);

        let startTime = Date.now();
        const duration = 2000; // 2 seconds

        Object.keys(NUCLEAR_EFFECTS).forEach(effect => {
        const baseDuration = 2000;
        const totalDuration = baseDuration + NUCLEAR_EFFECTS[effect].addedDuration;
        const startDelay = NUCLEAR_EFFECTS[effect].order * 200; // Stagger start times

        setTimeout(() => {
            const animationStart = Date.now();
            const interval = setInterval(() => {
                const currentTime = Date.now();
                const progress = Math.min((currentTime - animationStart) / totalDuration, 1);
                
                if (progress === 1) {
                    clearInterval(interval);
                    return;
                }

                const eased = easeOutCirc(progress);
                const finalRadius = calculateEffectRadius(kilotons, effect);
                const currentRadius = finalRadius * eased;
                
                if (!circles[effect]) {
                    circles[effect] = L.circle(csa, {
                        color: NUCLEAR_EFFECTS[effect].color,
                        fillColor: NUCLEAR_EFFECTS[effect].color,
                        fillOpacity: NUCLEAR_EFFECTS[effect].opacity,
                        radius: currentRadius
                    }).addTo(map);
                } else {
                    circles[effect].setLatLng(csa);
                    circles[effect].setRadius(currentRadius);
                }
            }, 16);
        }, startDelay);
    });

        const populationData = await getPopulationDensity(csa[0], csa[1], circle.getRadius());
        if (populationData) {
            const popMessage = `Estimated affected population: ${populationData.population.toLocaleString()}`;
            document.getElementById('error').innerHTML = popMessage;
        }
    });

    // Add legend
    const legend = L.control({position: 'bottomright'});
    legend.onAdd = function(map) {
        const div = L.DomUtil.create('div', 'legend');
        div.innerHTML = `
            <style>
                .legend {
                    background: white;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                .legend-item {
                    margin: 5px 0;
                }
                .legend-color {
                    display: inline-block;
                    width: 20px;
                    height: 20px;
                    margin-right: 5px;
                }
            </style>
        `;
        
        Object.entries(NUCLEAR_EFFECTS).forEach(([key, value]) => {
            div.innerHTML += `
                <div class="legend-item">
                    <span class="legend-color" style="background: ${value.color}"></span>
                    ${key.replace('_', ' ')}
                </div>
            `;
        });
        
        return div;
    };
    legend.addTo(map);
});