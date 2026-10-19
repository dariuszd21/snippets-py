{
  description = "Flake for python 3.14 development shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          devShells.default = pkgs.mkShell {
            packages = [ 
              pkgs.stdenv
              pkgs.python314
              pkgs.python314Packages.pytest
              pkgs.python314Packages.python-lsp-server
              pkgs.python314Packages.flit
              pkgs.ruff
            ];
            shellHook = ''
              export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib/"
            '';
          };
        }
      );
}

