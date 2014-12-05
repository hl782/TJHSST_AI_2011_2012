set terminal png
set output "projectile.png"
set title ""
set xlabel "x, meters"
set ylabel "y, meters"
set xtics nomirror
set ytics nomirror
plot "traj.txt" u 2:3 w l notitle,0 w l notitle
