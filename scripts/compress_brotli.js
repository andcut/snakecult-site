const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const exts = ['.html', '.css', '.js', '.svg', '.xml', '.json'];
const rootDir = path.join(__dirname, '..', 'public');

function compressFile(filePath) {
  const dest = filePath + '.br';
  if (fs.existsSync(dest)) return;
  const data = fs.readFileSync(filePath);
  const compressed = zlib.brotliCompressSync(data, {
    params: {
      [zlib.constants.BROTLI_PARAM_QUALITY]: 11,
    }
  });
  fs.writeFileSync(dest, compressed);
}

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath);
    } else if (exts.includes(path.extname(entry.name))) {
      compressFile(fullPath);
    }
  }
}

if (fs.existsSync(rootDir)) {
  walk(rootDir);
} else {
  console.error('public directory not found');
  process.exit(1);
}
