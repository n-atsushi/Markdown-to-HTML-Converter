import sys
import markdown

def covert_markdown(input_file,output_file):
    with open(input_file) as i_f:
        contents = i_f.read()
        html = markdown.markdown(contents)
        
        with open(output_file, 'w') as o_p:
            o_p.write(html)
            print(f'=== create {output_file} ===')

def main():
    cmd = {
       'markdown': [covert_markdown, 4],
    }    
    try:
        print(f'*** {sys.argv[1]} ***')
        
        func, arg_num = cmd.get(sys.argv[1])
        
        if func is None or len(sys.argv) < arg_num:
            raise Exception('Invalid arguments')
        
        if sys.argv[2][-3:] != '.md':
            raise Exception('Invalid arguments')
        
        func(*sys.argv[2:arg_num])
        
        print(f'*** Success {func.__name__} ***')
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()