document.addEventListener('DOMContentLoaded', () => {
    const schemeModal = document.getElementById('schemeModal');
    schemeModal.addEventListener('show.bs.modal', event => {
        const button = event.relatedTarget;
        const name = button.getAttribute('data-name');
        const category = button.getAttribute('data-category');
        const state = button.getAttribute('data-state');
        const summary = button.getAttribute('data-summary');
        const ministry = button.getAttribute('data-ministry');
        const year = button.getAttribute('data-year');

        const modalTitle = schemeModal.querySelector('.modal-title');
        const modalName = schemeModal.querySelector('#modal-name');
        const modalCategory = schemeModal.querySelector('#modal-category');
        const modalState = schemeModal.querySelector('#modal-state');
        const modalSummary = schemeModal.querySelector('#modal-summary');
        const modalMinistry = schemeModal.querySelector('#modal-ministry');
        const modalYear = schemeModal.querySelector('#modal-year');

        modalTitle.textContent = name;
        modalName.textContent = name;
        modalCategory.textContent = category;
        modalState.textContent = state;
        modalSummary.textContent = summary;
        modalMinistry.textContent = ministry;
        modalYear.textContent = year;
    });
});
