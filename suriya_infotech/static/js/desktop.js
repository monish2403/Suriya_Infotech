const buttons = document.querySelectorAll('.desktop-btn');
const cards = document.querySelectorAll('.desktop-card');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const selectedBrands = button.value;

        cards.forEach(card => {
            if(selectedBrands === 'all' || card.dataset.category === selectedBrands){
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        })
    })
})
