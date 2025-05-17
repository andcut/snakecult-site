const { execSync } = require('child_process');

function hasHugo() {
  try {
    execSync('hugo version', { stdio: 'ignore' });
    return true;
  } catch (err) {
    return false;
  }
}

if (!hasHugo()) {
  console.log('hugo command not found. Skipping build check.');
  process.exit(0);
}

try {
  execSync('hugo --minify --panicOnWarning', { stdio: 'inherit' });
} catch (err) {
  console.error('Hugo build failed');
  process.exit(1);
}
