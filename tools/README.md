## How to use the complex systems paper and press database for great good

### Include your press in a webpage

```html
<div id="putpresshere"></div>
<script type="text/javascript" src="http://cmplxsys.w3.uvm.edu/static/wordpress/js/plate.min.js"></script>
<script type="text/javascript" src="http://cmplxsys.w3.uvm.edu/static/wordpress/js/jquery-1.9.1.js"></script>
<script type="text/javascript" src="http://cmplxsys.w3.uvm.edu/static/wordpress/js/cmplxsys-functions.js"></script>
<script type="text/javascript">
personal_press_page("cdanforth","#putpresshere",press_list_template_allprojects);
</script>
```

Of course you can take the functions and templates in the `cmplxsys-functions.js` file and modify to your own liking.

### Include your papers and press in a LaTeX document

Usage: run this script with `python cmplxsys_press_and_papers_to_latex.py andyreagan`.

This a (longer) python script that will generate two `.tex` files that you can then input into a LaTeX document using (for the example here) `\input{andyreagan-cv.papers-cmplxsys}`.
Of course you can modify the templates here to format the press or papers to your liking.
It will locally save the images from the press and papers into a `figures` directory.
