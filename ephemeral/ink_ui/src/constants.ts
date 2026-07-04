export const APP_VERSION = process.env.EPHEMERAL_VERSION ?? 'dev';
export const smokeTest = process.argv.includes('--smoke-test');
export const animationFrames = ['·', '•', '◦', '•'];
