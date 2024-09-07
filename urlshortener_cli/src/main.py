from utils.my_args import get_args


if __name__ == '__main__':
   args = get_args()

   if args.minify:
       print('minify')
   elif args.expand:
       print('expand')

