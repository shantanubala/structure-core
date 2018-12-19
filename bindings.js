var structureCore;

// use the presence of a debug environment variable to decide which build to load
if (process.env.DEBUG) {
    structureCore = require('./build/Debug/structureCore.node');
}
else {
    structureCore = require('./build/Release/structureCore.node');
}

module.exports = structureCore;