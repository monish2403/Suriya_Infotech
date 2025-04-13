const buttons = document.querySelectorAll('.lap-btn');
const cards = document.querySelectorAll('.laptop-card');

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
