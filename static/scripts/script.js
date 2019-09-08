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
        });
    }
}