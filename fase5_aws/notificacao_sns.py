import os
import boto3


def enviar_alerta(mensagem, assunto="Alerta FarmTech 7"):
    topic_arn = os.getenv("FARMTECH_SNS_TOPIC_ARN")
    regiao = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")

    if not topic_arn:
        raise ValueError("Configure a variável FARMTECH_SNS_TOPIC_ARN.")

    if not regiao:
        raise ValueError("Configure a variável AWS_REGION.")

    sns = boto3.client("sns", region_name=regiao)

    resposta = sns.publish(
        TopicArn=topic_arn,
        Subject=assunto,
        Message=mensagem,
    )

    return resposta.get("MessageId")