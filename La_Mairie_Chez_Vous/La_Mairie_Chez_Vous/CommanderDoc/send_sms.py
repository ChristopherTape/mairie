import logging
from twilio.rest import Client
from django.conf import settings
from .models import FormulaireDemandeActeNaissance  # Assurez-vous d'importer le modèle approprié

logger = logging.getLogger(__name__)

def sendsms(commande_id):
    logger.info("Préparation de l'envoi du SMS")
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    try:
        # Récupérer la commande depuis la base de données
        commande = FormulaireDemandeActeNaissance.objects.get(id=commande_id)
        to_number = commande.tel

        if commande.livraison == 'presentiel':
            message_body = (
                f"Votre commande #{commande_id} est terminée. "
                f"Vous pouvez venir récupérer votre commande."
                f"merci d'avoir utiliser la_mairie_chez_vous"
            )
        elif commande.livraison == 'point de relais':
            message_body = (
                f"Votre commande #{commande_id} est terminée. "
                f"Vous pouvez aller la récupérer dans votre point de relais choisi : {commande.ville_de_livraison}."
                f"merci d'avoir utiliser la_mairie_chez_vous"
            )
        elif commande.livraison == 'livraison':
            message_body = (
                f"Votre commande #{commande_id} est terminée. "
                f"Un agent de livraison viendra vous livrer à cette adresse : {commande.ville_de_livraison}."
                f"merci d'avoir utiliser la_mairie_chez_vous"
            )
        else:
            message_body = (
                f"Votre commande #{commande_id} est terminée. "
                "Merci d'avoir utilisé notre application la_mairie_chez_vous 😊"
            )

        # Envoyer le SMS
        message = client.messages.create(
            body=message_body,
            from_='+14177886788',  # Remplacez par votre numéro Twilio vérifié
            to=to_number,
        )

        logger.info(f"SMS envoyé : {message.sid}")
        print("Votre commande est terminée, vous pouvez la récupérer à l'adresse marquée sur votre reçu.")
    except FormulaireDemandeActeNaissance.DoesNotExist:
        logger.error(f"Commande avec l'ID {commande_id} n'existe pas.")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi du SMS : {str(e)}")


logger = logging.getLogger(__name__)

def sendsms_refus(commande_id):
    logger.info("Préparation de l'envoi du SMS")
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    try:
        # Récupérer la commande depuis la base de données
        commande = FormulaireDemandeActeNaissance.objects.get(id=commande_id)
        to_number = commande.tel
        message_body = (
            f"Votre commande #{commande_id} a été refusée, "
            "motif: incohérence des informations. "
            "Vous serez remboursé dans de brefs délais."
        )

        message = client.messages.create(
            body=message_body,
            from_='+14177886788',  # Remplacez par votre numéro Twilio vérifié
            to=to_number,
        )

        logger.info(f"SMS envoyé : {message.sid}")
    except FormulaireDemandeActeNaissance.DoesNotExist:
        logger.error(f"Commande avec l'ID {commande_id} n'existe pas.")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi du SMS : {str(e)}")