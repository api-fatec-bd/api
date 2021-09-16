
from conexaoMongoDB import selectBanco


#CRIAÇÃO DE FILTTROS PARA IMPLEMENTAR O BANCO QUE SERÁ ENVIADO AO DW

#COLLECTION STATISTICS
def selectCollectionStatistics():
    statistics = selectBanco().rocketchat_statistics

    #CRIAR FILTROS AQUI

    return statistics


#COLLECTION CRON HISTORY
def selectCollectionCronHistory():
    cron_history = selectBanco().rocketchat_cron_history


    #CRIAR FILTROS AQUI

    return cron_history