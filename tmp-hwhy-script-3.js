
        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');

        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Sticky Header Logic
        let lastScrollTop = 0;
        const header = document.getElementById('main-header');
        window.addEventListener('scroll', function() {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (scrollTop > lastScrollTop && scrollTop > 100) { header.classList.add('header-hidden'); } 
            else { header.classList.remove('header-hidden'); }
            lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
        });

    
