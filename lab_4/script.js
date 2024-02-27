let productCounter = 1;  // Инициализируем счетчик

class Product {
    constructor(id, name, price, currency, imageUrl) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.currency = currency;
        this.imageUrl = imageUrl;
        this.productElement = this.createProductElement();
        this.deleteButton = null;
    }

    createProductElement() {
        const productElement = document.createElement('div');
        productElement.className = 'product';

        const imgElement = document.createElement('img');
        imgElement.src = this.imageUrl;
        imgElement.alt = this.name;
        productElement.appendChild(imgElement);

        const nameElement = document.createElement('h3');
        nameElement.textContent = this.name;
        productElement.appendChild(nameElement);

        const priceElement = document.createElement('p');
        priceElement.textContent = `${this.price} ${this.currency}`;
        productElement.appendChild(priceElement);

        const addToCartButton = new Button('В корзину', () => this.addToCart());
        productElement.appendChild(addToCartButton.getElement());

        return productElement;
    }

    addToCatalog() {
        const catalog = document.getElementById('catalog');
        catalog.appendChild(this.productElement);
    }

    removeFromCatalog() {
        const catalog = document.getElementById('catalog');
        catalog.removeChild(this.productElement);
        if (this.deleteButton) {
            this.deleteButton.removeButton();

        }
    }

    setProductImage(imageUrl) {
        const imgElement = this.productElement.querySelector('img');
        imgElement.src = imageUrl;
    }

    setProductName(name) {
        const nameElement = this.productElement.querySelector('h3');
        nameElement.textContent = name;
    }

    setProductPrice(price, currency) {
        const priceElement = this.productElement.querySelector('p');
        priceElement.textContent = `${price} ${currency}`;
    }

    addToCart() {
        // Логика добавления товара в корзину
        console.log(`Product ${this.name} added to cart.`);
    }
}


class Button {
    constructor(text, clickHandler) {
        this.text = text;
        this.clickHandler = clickHandler;
        this.buttonElement = this.createButtonElement();
    }

    createButtonElement() {
        const buttonElement = document.createElement('button');
        buttonElement.className = 'button';
        buttonElement.textContent = this.text;
        buttonElement.addEventListener('click', this.clickHandler);
        return buttonElement;
    }

    getElement() {
        return this.buttonElement;
    }


    removeButton() {
        this.buttonElement.removeEventListener('click', this.clickHandler);
        this.buttonElement.parentNode.removeChild(this.buttonElement);
    }

    setButtonSize(width, height) {
        this.buttonElement.style.width = `${width}px`;
        this.buttonElement.style.height = `${height}px`;
    }

    setButtonBackground(color) {
        this.buttonElement.style.backgroundColor = color;
    }

    setButtonText(text) {
        this.buttonElement.textContent = text;
    }
}


const createButton = new Button('Создать объявление', createNewProduct);
document.body.appendChild(createButton.getElement());

function createNewProduct() {
    const name = prompt('Введите название товара:');
    const price = parseFloat(prompt('Введите цену товара:'));
    const currency = prompt('Введите валюту товара (USD, BYN, RUB):');
    const imageUrl = prompt('Введите URL изображения товара:');

    const newProduct = new Product(productCounter++, name, price, currency, imageUrl);
    newProduct.addToCatalog();

    const deleteButton = new Button('Удалить', () => newProduct.removeFromCatalog());
    newProduct.deleteButton = deleteButton;

    document.body.appendChild(deleteButton.getElement());
}

