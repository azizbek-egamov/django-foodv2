const urlParams = new URLSearchParams(window.location.search);
const userId = urlParams.get('user_id');

function adjustContainerHeight() {
    const container = document.querySelector('.order-container');
    const orderItems = document.querySelectorAll('.order-item');
    
    const containerHeight = orderItems.length * 80 + 200; // Har bir order-item uchun 80px, header va comment uchun 200px
    
    container.style.height = containerHeight + 'px';

    var totalPrices = document.querySelectorAll('.item-price');
    var totalSum = Array.from(totalPrices).reduce((sum, price) => sum + parseFloat(price.textContent), 0);

    var payButton = document.querySelector('.pay-buttonn');
    payButton.textContent = `Перейти к оплате: ${totalSum.toFixed(2)} сум`;
}

// Sahifa yuklangandan so'ng container balandligini sozlash
window.addEventListener('load', adjustContainerHeight);

if (userId) {
    let links = document.querySelectorAll('.uyt');
    let linkss = document.querySelectorAll('.pay-buttonn');

    links.forEach(link => {
        let baseHref = link.getAttribute('href') || '';

        link.setAttribute('href', `${baseHref}?user_id=${userId}`);
    });

    linkss.forEach(link => {
        link.setAttribute('href', `https://t.me/fastfoodv2bot?start=payment--${userId}`);
    });
    // document.getElementById('content').classList.remove('blov');
} else {
    console.log('User ID parametri topilmadi.');
}