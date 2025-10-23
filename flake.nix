{
  description = "Bootcamp Python environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs   = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        python313
        python313Packages.pip
        python313Packages.virtualenv
        python313Packages.numpy
      ];

      shellHook = ''
        if [ ! -d .venv ]; then
          python -m venv .venv
        fi
        . .venv/bin/activate
        python -m pip install --upgrade pip
        echo "🐍 Python: $(python --version)  |  Venv: .venv active"
      '';
    };
  };
}
