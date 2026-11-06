// Post Affiliate Pro click tracking + Stripe referral hand-off for payyourselffirst.com.
// Records referral visits (?a_aid=...) and adds the PAP visitor ID to Stripe Payment
// Links as client_reference_id, so the PAP Stripe plugin credits the right affiliate.
(function () {
    if (window.__pyfPapLoaded) return;
    window.__pyfPapLoaded = true;
    var ACCOUNT = 'default1';
    var visitorId = '';

    function tag(link) {
        if (!visitorId || !link || !link.href || link.href.indexOf('buy.stripe.com') === -1) return;
        if (link.href.indexOf('client_reference_id=') !== -1) return;
        link.href += (link.href.indexOf('?') !== -1 ? '&' : '?') + 'client_reference_id=' + ACCOUNT + visitorId;
    }
    function tagAll() {
        var links = document.querySelectorAll("a[href*='buy.stripe.com']");
        for (var i = 0; i < links.length; i++) tag(links[i]);
    }
    // Buttons added later by the page (CMS content) are tagged when clicked.
    document.addEventListener('click', function (e) {
        var el = e.target;
        while (el && el.tagName !== 'A') el = el.parentElement;
        if (el) tag(el);
    }, true);

    var s = document.createElement('script');
    s.type = 'text/javascript';
    s.id = 'pap_x2s6df8d';
    s.src = 'https://payyourselffirst.postaffiliatepro.com/scripts/ojyfma';
    s.onload = function () {
        try {
            PostAffTracker.setAccountId(ACCOUNT);
            PostAffTracker.executeOnResponseFinished.push(function () {
                visitorId = PostAffTracker.getVisitorId() || '';
                tagAll();
            });
            PostAffTracker.track();
        } catch (err) {}
    };
    document.body.appendChild(s);
})();
