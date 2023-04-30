function chooseCrypto(ele) {
    cryptoChoice.value = ele.dataset.crypto;

    // remove all active classes which are inside the crypto choice container
    document.querySelectorAll('.choice').forEach(function(choice) {
        if (choice.parentElement.id === 'cryptoChoice') {
            choice.classList.remove('active');
        }
    });

    ele.classList.add('active');
}

function chooseGiftCard(ele) {
    giftCardChoice.value = ele.dataset.giftcard;

    document.querySelectorAll('.choice').forEach(function(choice) {
        if (choice.parentElement.id === 'giftCardChoice') {
            choice.classList.remove('active');
        }
    });

    ele.classList.add('active');
}