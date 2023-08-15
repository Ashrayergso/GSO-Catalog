```javascript
// Function to filter products based on user input
function filterProducts() {
    let input = document.getElementById('searchInput').value.toUpperCase();
    let productCard = document.getElementsByClassName('product-card');

    for (let i = 0; i < productCard.length; i++) {
        let title = productCard[i].getElementsByClassName('product-title')[0];
        if (title) {
            let textValue = title.textContent || title.innerText;
            if (textValue.toUpperCase().indexOf(input) > -1) {
                productCard[i].style.display = "";
            } else {
                productCard[i].style.display = "none";
            }
        }
    }
}

// Function to sort products based on user selection
function sortProducts() {
    let select = document.getElementById('sortSelect');
    let selectedOption = select.options[select.selectedIndex].value;
    let productContainer = document.getElementById('productContainer');
    let productCard = productContainer.getElementsByClassName('product-card');

    let products = Array.from(productCard);
    products.sort((a, b) => {
        let aTitle = a.getElementsByClassName('product-title')[0].innerText;
        let bTitle = b.getElementsByClassName('product-title')[0].innerText;
        let aPrice = parseFloat(a.getElementsByClassName('product-price')[0].innerText.replace('$', ''));
        let bPrice = parseFloat(b.getElementsByClassName('product-price')[0].innerText.replace('$', ''));

        if (selectedOption === 'nameAsc') {
            return aTitle.localeCompare(bTitle);
        } else if (selectedOption === 'nameDesc') {
            return bTitle.localeCompare(aTitle);
        } else if (selectedOption === 'priceAsc') {
            return aPrice - bPrice;
        } else if (selectedOption === 'priceDesc') {
            return bPrice - aPrice;
        }
    });

    for (let i = 0; i < products.length; i++) {
        productContainer.appendChild(products[i]);
    }
}

// Event listeners for filter and sort functions
document.getElementById('searchInput').addEventListener('keyup', filterProducts);
document.getElementById('sortSelect').addEventListener('change', sortProducts);
```