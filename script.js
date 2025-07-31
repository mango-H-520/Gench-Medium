// 菜单按钮交互
const menuBtn = document.getElementById('menuBtn');
const mainNav = document.getElementById('mainNav');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('open');
    mainNav.style.display = mainNav.style.display === 'flex' ? 'none' : 'flex';
});

// 窗口大小变化时重置导航状态
window.addEventListener('resize', () => {
    if (window.innerWidth >= 992) {
        mainNav.style.display = 'flex';
        menuBtn.classList.remove('open');
    } else {
        mainNav.style.display = 'none';
    }
});