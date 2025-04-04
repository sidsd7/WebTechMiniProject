window.onload = () => {
    const artistImages = [
        'https://variety.com/wp-content/uploads/2024/02/Eminem.jpg',
        'https://www.shutterstock.com/editorial/image-editorial/M6T6M553N7T7U6z6MTMxODE=/taylor-swift-440nw-13831852dt.jpg',
        'https://render.fineartamerica.com/images/images-profile-flow/400/images/artworkimages/mediumlarge/2/1-elvis-presley-archive-photos.jpg',
        'https://media.gettyimages.com/id/466166885/photo/new-york-singer-michael-jackson-posing-for-a-portrait-on-september-9-1988-in-new-york-new-york.jpg?s=612x612&w=gi&k=20&c=5R9Gh6j9gDTs0p5J-2TQYmc41GhZvr2dGa85DjCN2xk=',
        'https://ew.com/thmb/WhmFKloYCWVKMkDBrMeYCHQtPcU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bruno-mars_0-4d3e8ba6593f403d85083e85810086db.jpg',
        'https://static01.nyt.com/images/2014/08/24/arts/24GRANDE1/24JPGRANDE1-superJumbo.jpg',
        'https://cdn.britannica.com/16/262416-050-7E966413/selena-gomez-attends-the-emilia-perez-photocall-at-the-77th-annual-cannes-film-festival-2024.jpg',
        'https://assets.vogue.com/photos/609bb445758287e5e091eeed/master/pass/Billie-Eilish-Happier-Than-Ever.jpeg',
        'https://i.scdn.co/image/ab67616d0000b273b627441824c5d0748c8cb077',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFkYHn6tWG4KYBXLMANz77kX_LcwojTEXJjA&s',
        'https://pyxis.nymag.com/v1/imgs/ef6/6fe/c126de3c9e2afa273d7af54056c73eda10-shawn-mendes-feature-lede.2x.rvertical.w512.jpg',
        'https://i.scdn.co/image/ab67616d0000b273897f73256b9128a9d70eaf66',
        'https://www.usmagazine.com/wp-content/uploads/2020/10/Harry-Styles-Hair-Evolution-Through-The-Years-Slide-4.jpg?quality=62&strip=all',
        'https://www.hollywoodreporter.com/wp-content/uploads/2012/03/justin-bieber-pr-2012-l.jpg?w=1440&h=810&crop=1',
        'https://c.files.bbci.co.uk/5e57/live/88fd3480-49ad-11ef-8957-57bc56098a6f.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAbYd95dPuVdpFfSu0v3scRW2vwRSEMQatAQ&s',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9xwddXAAp6gEg5wulRxsy04UHO07lVMPPaw&s',
        'https://c8.alamy.com/comp/D074GR/rihanna-us-singer-in-november-2012-photo-jeffrey-mayer-D074GR.jpg'
    ];

    const container = document.querySelector('.artist-background');
    
    const row1 = document.createElement('div');
    row1.className = 'artist-row row1';
    const row2 = document.createElement('div');
    row2.className = 'artist-row row2';

    const row1Content = document.createElement('div');
    row1Content.className = 'artist-row-content';
    const row2Content = document.createElement('div');
    row2Content.className = 'artist-row-content';

    const shuffledImages = [...artistImages].sort(() => Math.random() - 0.5);
    const midPoint = Math.ceil(shuffledImages.length / 2);
    

    const row1Images = shuffledImages.slice(0, midPoint);
    row1Images.forEach((src) => {
        const img = document.createElement('img');
        img.src = src;
        row1Content.appendChild(img);
    });

    row1Images.forEach((src) => {
        const img = document.createElement('img');
        img.src = src;
        row1Content.appendChild(img);
    });

    const row2Images = shuffledImages.slice(midPoint);
    row2Images.forEach((src) => {
        const img = document.createElement('img');
        img.src = src;
        row2Content.appendChild(img);
    });
    
    row2Images.forEach((src) => {
        const img = document.createElement('img');
        img.src = src;
        row2Content.appendChild(img);
    });

    row1.appendChild(row1Content);
    row2.appendChild(row2Content);
    container.appendChild(row1);
    container.appendChild(row2);
};
