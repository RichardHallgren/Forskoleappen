import forskoleappen
import sys

folder_path = sys.argv[1]

forskoleappen.read_local_data(path = folder_path)

forskoleappen.prep_and_visualize(local_read = True, days='All')
