set terminal png
set output "demo.png"
set xrange[0:1]
set yrange[0:1]
set xlabel "p, density"
set ylabel "% spanning"
set title "Spanning Plot (almost)"
plot "data.txt" with lines notitle
