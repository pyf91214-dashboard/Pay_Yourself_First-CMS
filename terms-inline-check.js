
        const backToTopBtn = document.getElementById('backToTopBtn');

        // Show/Hide logic based on scroll position
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) { // Show after scrolling down 300px
                backToTopBtn.classList.remove('translate-y-20', 'opacity-0');
            } else {
                backToTopBtn.classList.add('translate-y-20', 'opacity-0');
            }
        });

        // Smooth scroll to top function
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }
    
