for i in `seq 1 50`;
do
    python guppy.py > ../output/default_$i.txt
    python guppy.py --no_r  > ../output/no_r_$i.txt
    python guppy.py --no_c > ../output/no_c_$i.txt
    python guppy.py --no_p > ../output/no_p_$i.txt
done

wait $!

python cleanup.py ../output/default_*.txt > ../data/default_avg.txt
python cleanup.py ../output/no_r_*.txt > ../data/no_r_avg.txt
python cleanup.py ../output/no_c_*.txt > ../data/no_c_avg.txt
python cleanup.py ../output/no_p_*.txt > ../data/no_p_avg.txt
