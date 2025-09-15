import puppeteer from 'puppeteer';

const browser = await puppeteer.launch({ headless: false });
const page = await browser.newPage();

await page.setViewport({ width: 1920, height: 1080 });
await page.goto('http://localhost:5173', { waitUntil: 'networkidle2' });

// 等待页面完全加载
await page.waitForTimeout(2000);

// 截图
await page.screenshot({ 
  path: 'xlerobot-ui.png',
  fullPage: true 
});

console.log('Screenshot saved as xlerobot-ui.png');
await browser.close();