// 作品过滤功能
document.addEventListener('DOMContentLoaded', function() {
    const tagButtons = document.querySelectorAll('.tag-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    const modal = document.getElementById('image-modal');
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalAuthor = document.getElementById('modal-author');
    const modalDescription = document.getElementById('modal-description');
    const closeBtn = document.querySelector('.close-btn');
    const imgContainers = document.querySelectorAll('.gallery-img-container');
    
    // 作品描述数据（实际应用中可从服务器获取）
    const imageDescriptions = {
        'work1.jpg': '记录了校园艺术节的精彩瞬间，展现了同学们的艺术才华与创造力。',
        'work2.jpg': '四季更迭中的校园美景，每一张照片都捕捉了不同季节的独特韵味。',
        'work3.jpg': '校园人物肖像系列，通过镜头展现师生们的精神风貌。',
        'work4.jpg': '校园文创产品宣传拍摄，突出产品特色与校园文化内涵。',
        'work5.jpg': '',
        'work6.jpg': '图书馆日落时分的美丽景色，知识的殿堂与自然之美交相辉映。'
    };
    
    // 标签过滤功能
    tagButtons.forEach(button => {
        button.addEventListener('click', function() {
            // 移除所有标签的active类
            tagButtons.forEach(btn => btn.classList.remove('active'));
            // 给当前点击的标签添加active类
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            // 过滤作品
            galleryItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
    
    // 图片点击放大功能
    imgContainers.forEach(container => {
        container.addEventListener('click', function() {
            const img = this.querySelector('.gallery-img');
            const item = this.closest('.gallery-item');
            const title = item.querySelector('h4').textContent;
            const author = item.querySelector('.author').textContent;
            
            // 获取图片文件名用于匹配描述
            const imgSrc = img.getAttribute('src');
            const imgName = imgSrc.split('/').pop();
            const description = imageDescriptions[imgName] || '这是一幅精彩的摄影作品';
            
            // 设置模态框内容
            modalImg.setAttribute('src', imgSrc);
            modalTitle.textContent = title;
            modalAuthor.textContent = author;
            modalDescription.textContent = description;
            
            // 显示模态框
            modal.style.display = 'block';
            // 阻止页面滚动
            document.body.style.overflow = 'hidden';
        });
    });
    
    // 关闭模态框
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        // 恢复页面滚动
        document.body.style.overflow = 'auto';
    });
    
    // 点击模态框外部关闭
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
    
    // 键盘ESC关闭模态框
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
});