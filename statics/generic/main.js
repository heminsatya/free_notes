// Document loaded
document.addEventListener('DOMContentLoaded', function() {

    // Navigation active class
    const page_url = window.location.pathname;
    const nav_elems = document.querySelectorAll('.navbar-nav a');
    if (nav_elems) {
        for (let i = 0; i < nav_elems.length; i++) {
            // Add active class to index page
            if (page_url == '/') {
                nav_elems[0].classList.add('active');
    
            // Add active class to current page nav
            } else if (nav_elems[i].getAttribute('href') == page_url) {
                nav_elems[i].classList.add('active');
    
            // remove inactive nav
            } else {
                nav_elems[i].classList.remove('active');
            }
        }
    }


    // Main content height
    const windowHeight = window.innerHeight;
    let headerHeight = document.querySelector('.header');
    let footerHeight = document.querySelector('.footer');
    if (headerHeight && footerHeight) {
        headerHeight = headerHeight.getBoundingClientRect().height;
        footerHeight = footerHeight.getBoundingClientRect().height;

        const mainHeight = windowHeight - (headerHeight + footerHeight) - (64);

        document.querySelector('.main').style.minHeight = mainHeight + 'px';
    }

});
