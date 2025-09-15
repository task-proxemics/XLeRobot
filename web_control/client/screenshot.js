const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: false
  });
  const page = await browser.newPage();
  
  // 设置视口大小
  await page.setViewport({
    width: 1920,
    height: 1080
  });
  
  // 访问页面
  await page.goto('http://localhost:5173', {
    waitUntil: 'networkidle2'
  });
  
  // 等待页面加载
  await page.waitForTimeout(2000);
  
  // 截图
  await page.screenshot({
    path: 'ui-screenshot.png',
    fullPage: true
  });
  
  console.log('Screenshot saved as ui-screenshot.png');
  
  await browser.close();
})();