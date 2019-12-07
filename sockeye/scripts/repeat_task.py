import argparse
import itertools
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--vocab', '-v', type=int, required=True)
parser.add_argument('--num', '-n', type=int, required=True)
parser.add_argument('--repeats', '-r', type=int, required=True)
parser.add_argument('--min-length', '-l', type=int, required=True)
parser.add_argument('--max-length', '-L', type=int, required=True)
parser.add_argument('--prefix', '-p', type=str, required=True)
parser.add_argument('--step', '-s', default=1, type=int, required=False)
args = parser.parse_args()

filename = "repeat_n%d_v%d_l%d-%d_r%d_s%d_%s" % (args.num, args.vocab, args.min_length, args.max_length, args.repeats, args.step, args.prefix)
with open(filename + ".src", "wt") as src, open(filename + ".tgt", "wt") as tgt:
    for i in range(args.num):
        r = np.random.choice(list(range(0, args.repeats, 1)))
        
        length = np.random.randint(args.min_length, args.max_length)
        array = [str(np.random.randint(args.vocab)) for _ in range(length)]
        arrays = list(itertools.chain(*itertools.repeat(array, args.step * r + 1)))

        # src
        src.write("%s\n" % ' '.join([str(r)] + array))
        # tgt
        tgt.write("%s\n" % ' '.join(arrays))
        
