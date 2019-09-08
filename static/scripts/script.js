window.onload = () => {
    document.getElementById("navBurger").addEventListener('click', () => {
        document.getElementById("navBurger").classList.toggle('is-active');
        document.getElementById("navMenu").classList.toggle('is-active');
    });

    let stockSelectors = document.getElementsByClassName('stock-selector');
    for (let i = 0; i < stockSelectors.length; i++) {
        stockSelectors.item(i).addEventListener('click', e => {
            const stock = e.target.innerHTML;
            document.getElementById('stockName').innerHTML = stock;
            let imgSrc = document.getElementById('stockImage').src;
            imgSrc = imgSrc.split('/');
            imgSrc.pop();
            imgSrc.push(stock + '.png');
            imgSrc = imgSrc.join('/');
            document.getElementById('stockImage').src = imgSrc;
            document.getElementById('stockInfo').innerHTML = stocksInfo[stock] || "Sorry, no stock information available";
        });
    }
}

stocksInfo = {
    UPS: 'Stock prices will most likely increase slightly. It is advisable to invest in this stock.',
    AAPL: 'Stock prices will most likely decrease slightly. It is not advisable to invest in this stock.',
    AMZN: 'Stock prices will most likely remain stable. It is advisable to find a better stock.',
    COST: 'Stock prices will most likely decrease heavily. It is not advisable to invest in this stock.',
    CVS: 'Stock prices will most likely fluctuate but remain stable. It is advisable to find a better stock.',
    EBAY: 'Stock prices will most likely remain stable. It is advisable to find a better stock.',
    IBM: 'Stock prices will most likely remain stable. It is advisable to find a better stock.',
}