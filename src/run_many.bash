for i in `seq 1 50`;
do
    python guppy.py -c 0.1 > ../output/Crun_$i.txt
    python guppy.py -s 0.3 > ../output/Srun_$i.txt
done

python cleanup.py ../output/Crun_*.txt > ../data/Crun_avg.txt
python cleanup.py ../output/Srun_*.txt > ../data/Srun_avg.txt
