import json

app = "app"

__version__ = "2.0.0"

features = [
    "feature1",
]


def main():
    output = {
        "app": app,
        "version": __version__,
        "features": features,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
