def cripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'Aa':
            tradutor += '&'
        elif letra in 'Bb':
            tradutor += '*'    
        elif letra in 'Cc':
            tradutor += '+'    
        elif letra in 'Dd':
            tradutor += '@'    
        elif letra in 'Ee':
            tradutor += '!'    
        elif letra in 'Ff':
            tradutor += '-'
        elif letra in 'Gg':
            tradutor += '#'    
        elif letra in 'Hh':
            tradutor += '₡'    
        elif letra in 'Ii':
            tradutor += '✓'
        elif letra in 'Jj':
            tradutor += '×'
        elif letra in 'Kk':
            tradutor += '€'
        elif letra in 'Ll':
            tradutor += '|'
        elif letra in 'Mm':
            tradutor += '^'
        elif letra in 'Nn':
            tradutor += '∆'    
        elif letra in 'Oo':
            tradutor += '5'    
        elif letra in 'Pp':
            tradutor += ';'
        elif letra in 'Qq':
            tradutor += 'π'
        elif letra in 'Rr':
            tradutor += '©'
        elif letra in 'Ss':
            tradutor += '₲'
        elif letra in 'Tt':
            tradutor += '™'
        elif letra in 'Uu':
            tradutor += '2'    
        elif letra in 'Vv':
            tradutor += '>'    
        elif letra in 'Ww':
            tradutor += '<'    
        elif letra in 'Xx':
            tradutor += '•'    
        elif letra in 'Yy':
            tradutor += '°' 
        elif letra in 'Zz':
            tradutor += '$'       
        else:
            tradutor += letra
    return tradutor
 
       
mensagem = str(input('Coloque a mensagem: '))
print()
print('#'*40)
print()


print(f'MENSAGEM CRIPTOGRAFADA\n\n {cripto(mensagem)}')        
