def notas (*n, sit=False):
    """função que mostra dados da sua nota, como total/maior/menor/media e 
       opcionalmente a situação de acordo com sua media.

    ARGUMENTOS:
         notas(n, sit=false)

         :param n: uma ou mais notas dos alunos ( aceita várias notas )
         :param sit: mostra a situação do aluno pela media ( opcional )
         :return: dicionário com dados de varios alunos e situação de uma turma )
   
    """
    r = dict()
    r['total']= len(n)
    r['maior']= max(n)
    r['menor']= min(n)
    r['media']= sum(n)/len(n)

    if sit == True:
        if r['media'] >= 7:
            r['situação']= 'BOA'
        elif r['media'] >= 5:
            r['situação']= 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
        



resp = notas(5.3, 9.0, 7.8, sit=True)
help(notas)