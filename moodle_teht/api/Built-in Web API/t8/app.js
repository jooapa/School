document
  .getElementById("analyze-button")
  .addEventListener("click", async () => {
    const startDate =
      new Date(document.getElementById("start-date").value).getTime() / 1000;
    const endDate =
      new Date(document.getElementById("end-date").value).getTime() / 1000 +
      3600; // Add 1 hour to ensure end date data

    const response = await fetch(
      `https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=${startDate}&to=${endDate}`
    );
    const data = await response.json();

    const prices = data.prices;
    const volumes = data.total_volumes;

    const longestBearishTrend = getLongestBearishTrend(prices);
    const highestVolumeDay = getHighestVolumeDay(volumes);
    const bestBuySellDays = getBestBuySellDays(prices);

    displayResults(longestBearishTrend, highestVolumeDay, bestBuySellDays);
  });

function getLongestBearishTrend(prices) {
  let maxTrend = 0;
  let currentTrend = 0;

  for (let i = 1; i < prices.length; i++) {
    if (prices[i][1] < prices[i - 1][1]) {
      currentTrend++;
      if (currentTrend > maxTrend) {
        maxTrend = currentTrend;
      }
    } else {
      currentTrend = 0;
    }
  }

  return maxTrend;
}

function getHighestVolumeDay(volumes) {
  let maxVolume = 0;
  let maxVolumeDay = null;

  volumes.forEach((volume) => {
    if (volume[1] > maxVolume) {
      maxVolume = volume[1];
      maxVolumeDay = new Date(volume[0]).toISOString().split("T")[0];
    }
  });

  return { date: maxVolumeDay, volume: maxVolume };
}

function getBestBuySellDays(prices) {
  let minPrice = Infinity;
  let minPriceDay = null;
  let maxProfit = 0;
  let buyDay = null;
  let sellDay = null;

  prices.forEach((price) => {
    if (price[1] < minPrice) {
      minPrice = price[1];
      minPriceDay = new Date(price[0]).toISOString().split("T")[0];
    }

    const profit = price[1] - minPrice;
    if (profit > maxProfit) {
      maxProfit = profit;
      buyDay = minPriceDay;
      sellDay = new Date(price[0]).toISOString().split("T")[0];
    }
  });

  if (maxProfit === 0) {
    return { buy: null, sell: null };
  }

  return { buy: buyDay, sell: sellDay };
}

function displayResults(
  longestBearishTrend,
  highestVolumeDay,
  bestBuySellDays
) {
  const results = document.getElementById("results");
  results.innerHTML = `
    <p>Pisin laskutrendi: ${longestBearishTrend} päivää</p>
        <p>Korkein kaupankäyntivolyymi: ${highestVolumeDay.date} €${
    highestVolumeDay.volume
  }</p>
        <p>Paras aika ostaa: ${bestBuySellDays.buy || "N/A"}</p>
        <p>Paras aika myyä: ${bestBuySellDays.sell || "N/A"}</p>
    `;
}
