const load = () => {
    const { urls } = window;
    const {books} = urls;
    document.body.innerHTML += '<div id="loading">loading...</div>';

    fetch(books)
        .then(response => response.json())
        .then(books => {
            document.querySelector('.books-list').innerHTML =
                books
                    .map(book => `<li>${book.title}</li>`)
                    .join('');
            document.querySelector("#loading").remove();
        });
};

load();
