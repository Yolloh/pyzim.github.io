# pyzim.github.io
Proposed pyzim community website

This site is created using [Pelican](http://docs.getpelican.com/en/stable) and the [dopetrope](https://html5up.net/dopetrope) theme. To contribute you would like to first checkout pelican and how it works. 
Pages are generated from markdown and the hosting is done with [github pages](https://pages.github.com).


## Development

Clone the repository.

    git clone https://github.com/Pyzim/pyzim.github.io

Switch to the `source` branch.

    cd pyzim.github.io
    git checkout source

Install dependencies.

    pip install -r requirements.txt

hack! hack! hack! hack!

Run the devserver.

    make devserver

Now you can browse the website at `http://localhost:8000/`.

## Deployment

For deploying the website, the rendered HTML needs to be pushed to the `master`
branch. This can be done via the `Makefile` and the `ghp-import` script:

    make clean html
    make github

The current version should be live now.
