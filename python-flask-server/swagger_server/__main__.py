#!/usr/bin/env python3

import connexion




def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Face'})
    app.run(port=7000)


if __name__ == '__main__':
    main()
