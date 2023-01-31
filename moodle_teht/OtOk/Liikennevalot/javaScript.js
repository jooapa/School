const myImage = new Image(100, 200);
var i = undefined
const sleep = (time) => {
	return new Promise((resolve) => setTimeout(resolve, time))
  }

  	car1Exist = false
	car1Stop = false
  	car2Exist = false
	car2Stop = false
  	car3Exist = false
	car3Stop = false
  	car4Exist = false
	car4Stop = false

	var car1id = null;
	var car2id = null;
	var car3id = null;
	var car4id = null;


	function change(){

		var elem = document.getElementById("myButton1");
			if (elem.value=="Punainen"){
				elem.value = "Vihreä";
			}
			else{
				elem.value = "Punainen";
				imgContainer.appendChild(sourceImage.cloneNode(true));
			} 
	}	

	

	function GFG_Fun() {

		var img = document.createElement('img');
		img.src = "trafficlight.png";
		img.style.width = "auto";
		img.style.height = "50px";




		var img = document.createElement('img');
		img.src = 'car.png';
		img.style.width = "auto";
		img.style.height = "50px";
		img.style.position = "absolute";

		rng = Math.floor(Math.random() * 4);

		console.log(rng)
		if(rng == 0 && car1Exist == false){let pos = 0
			img.style.transform = "translate(204px, 400px)";
			document.getElementById('myContainer').appendChild(img);
			
			car1Exist = true
			clearInterval(car1id);car1id = setInterval(car1frame, 10);
			function car1frame() {if (pos == 120) {
				clearInterval(car1id);
				console.log("Stopped"); car1Stop = true
			  } else {pos++; 
				img.style.top = -pos + 'px'; car1Stop = false
			  }
			}
		}

		if(rng == 1 && car2Exist == false){let pos = 0;
			img.style.transform = "translate(410px, 160px)";
			img.style.transform += "rotate(-90deg)";
			document.getElementById('myContainer').appendChild(img);
			
			car2Exist = true
			
			clearInterval(car2id);car2id = setInterval(car2frame, 10);
			function car2frame() {if (pos == 120) {
				clearInterval(car2id);
				console.log("Stopped"); car2Stop = true
			  } else {pos++; 
				img.style.left = -pos + 'px'; car2Stop = false
			  }
			}
		}
		
		if(rng == 2 && car3Exist == false){let pos = 0;
			img.style.transform = "translate(160px, -30px)";
			img.style.transform += "rotate(180deg)";
			document.getElementById('myContainer').appendChild(img);
			
			car3Exist = true
			
			clearInterval(car3id);car3id = setInterval(car3frame, 10);
			function car3frame() {if (pos == 120) {
				clearInterval(car3id);
				console.log("Stopped"); car3Stop = true
			  } else {pos++; 
				img.style.top = pos + 'px'; car3Stop = false
			  }
			}
		}
		
		if(rng == 3 && car4Exist == false){let pos = 0;
			img.style.transform = "translate(-20px, 205px)";
			img.style.transform += "rotate(90deg)";
			document.getElementById('myContainer').appendChild(img);
			
			car4Exist = true
			
			clearInterval(car4id);car4id = setInterval(car4frame, 10);
			function car4frame() {if (pos == 120) {
				clearInterval(car4id);
				console.log("Stopped"); car4Stop = true
			} else {pos++; 
				img.style.left = pos + 'px'; car4Stop = false
			  }
			}
		}
	} 
	
	
	
	function TrafficLight(){
		var img1 = document.createElement('img');
		img1.src = 'redTR.png';
		img1.style.width = "auto";
		img1.style.height = "250px";
		img1.style.justifyContent = "center";
		img1.style.left = "-75px";
		img1.style.top = "50px";
		img1.style.position = "absolute";

		document.getElementById('ControllerChild').appendChild(img1);
		
		var img2 = document.createElement('img');
		img2.src = 'redTR.png';
		img2.style.width = "auto";
		img2.style.height = "250px";
		img2.style.left = "50px";
		img2.style.top = "50px";
		img2.style.position = "absolute";
		
		document.getElementById('ControllerChild').appendChild(img2);

		var img3 = document.createElement('img');
		img3.src = 'redTR.png';
		img3.style.width = "auto";
		img3.style.height = "250px";
		img3.style.justifyContent = "center";
		img3.style.left = "175px";
		img3.style.top = "50px";
		img3.style.position = "absolute";
		
		document.getElementById('ControllerChild').appendChild(img3);

		var img4 = document.createElement('img');
		img4.src = 'redTR.png';
		img4.style.width = "auto";
		img4.style.height = "250px";
		img4.style.justifyContent = "center";
		img4.style.left = "300px";
		img4.style.top = "50px";
		img4.style.position = "absolute";
		
		document.getElementById('ControllerChild').appendChild(img4);
	
}