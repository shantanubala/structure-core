{
    "targets": [{
        "target_name": "structureCore",
        "include_dirs": [
            "structure-sdk/x86_64/include",
            "structure-sdk/x86_64/include/ST",
            "src"
        ],
        "libraries": [
            "../structure-sdk/x86_64/lib/libStructureLinux.so"
        ],
        "sources": [
            "src/structure-core.cc"
        ]
    }]
}