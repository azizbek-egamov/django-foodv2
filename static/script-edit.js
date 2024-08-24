const urlParams = new URLSearchParams(window.location.search);
const userId = urlParams.get('user_id');

function updateQuantity(event, button, change) {
    event.preventDefault();
    var countSpan = button.parentNode.querySelector('.count');
    var countss = document.querySelector('.onsubmit');
    var currentCount = parseInt(countSpan.textContent);
    var newCount = currentCount + change;

    if (newCount >= 0) {
        countSpan.textContent = newCount;
        countSpan.style.animation = change <= 0 ? 'badge-incr 0.1s' : 'badge-decr 0.1s';
        countSpan.addEventListener('animationend', () => {
            countSpan.style.animation = '';
        });

        var oldName = countSpan.getAttribute('name');
        var nameParts = oldName.split('--');
        var newName = nameParts[0] + '--' + newCount;
        countSpan.setAttribute('name', newName);
    }

    var addToCartButton = document.querySelector('.submit');
    var ab = document.querySelector('.ab');
    var counts = document.querySelectorAll('.count');
    var totalCount = Array.from(counts).reduce((sum, count) => sum + parseInt(count.textContent), 0);

    if (totalCount >= 0) {
        addToCartButton.style.display = 'block';
        countss.style.display = 'none';
        // ab.style.display = 'none';

    } else {
        addToCartButton.style.display = 'block';
        countss.style.display = 'block';
        // ab.style.display = 'block';


    }

}

function submitOrder() {
    var counts = document.querySelectorAll('.count');
    var requests = [];

    counts.forEach(function (countSpan) {
        var count = parseInt(countSpan.textContent);
        if (count >= 0) {
            var nameAttr = countSpan.getAttribute('name');
            var code = nameAttr.split('--')[0];
            var url = `http://fastfood-toi.uz/api/user/updatefoods/?user_id=${userId}&code=${code}&count=${count}`;

            var request = fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data[0].status === "true") {
                        console.log(`Yuborildi: ${url}`);
                    } else {
                        console.error(`Xatolik yuz berdi: ${url}`);
                    }
                })
                .catch(error => console.error(`Fetch xatosi: ${error}`));

            requests.push(request);

            // countSpan.textContent = '0';    
            // var newName = `${code}--0`;
            // countSpan.setAttribute('name', newName);
        }
    });

    Promise.all(requests).then(() => {
        var addToCartButton = document.querySelector('.submit');
        var onaddToCartButton = document.querySelector('.onsubmit');
        addToCartButton.style.display = 'none';
        onaddToCartButton.style.display = 'block';
    });
}


let bodyHeight = document.body.offsetHeight;

let newHeight = bodyHeight + 40;

document.body.style.height = newHeight + 'px';

if (userId) {
    let links = document.querySelectorAll('.uyt');

    links.forEach(link => {
        let baseHref = link.getAttribute('href') || '';

        link.setAttribute('href', `${baseHref}?user_id=${userId}`);
    });
} else {
    console.log('User ID parametri topilmadi.');
}
