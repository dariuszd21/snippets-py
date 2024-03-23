{
  description = "Flake for python 3.11 development shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
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
              pkgs.stdenv pkgs.python311Full
              pkgs.python311Packages.pytest
              pkgs.python311Packages.python-lsp-server
              pkgs.python311Packages.flit
              pkgs.ruff
            ];
            shellHook = ''
              export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib/"
            '';
          };
        }
      );
}

