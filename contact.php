<?php
// Reçoit le formulaire de demande de devis et l'envoie à commercial@rancesales.com.
declare(strict_types=1);

$to = 'commercial@rancesales.com';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: /contact/');
    exit;
}

$lang = (($_POST['lang'] ?? 'fr') === 'en') ? 'en' : 'fr';
$back = $lang === 'en' ? '/en/contact/' : '/contact/';
$thanks = $lang === 'en' ? '/en/thanks/' : '/merci/';

// Champ piège anti-robots : rempli uniquement par les robots.
if (!empty($_POST['website'])) {
    header('Location: ' . $thanks);
    exit;
}

function field(string $key, int $max = 200): string
{
    $value = trim((string)($_POST[$key] ?? ''));
    $value = str_replace(["\r", "\n"], ' ', $value);
    return mb_substr($value, 0, $max);
}

$name = field('name', 120);
$company = field('company', 160);
$country = field('country', 40);
$email = filter_var(field('email', 200), FILTER_VALIDATE_EMAIL);
$phone = field('phone', 60);
$product = field('product', 120);
$volume = field('volume', 160);
$whatsapp = !empty($_POST['whatsapp']) ? 'Oui' : 'Non';
$message = mb_substr(trim((string)($_POST['message'] ?? '')), 0, 5000);

if ($name === '' || $email === false || $country === '') {
    header('Location: ' . $back . '?erreur=1#devis');
    exit;
}

$subjectText = 'Demande de devis : ' . ($company !== '' ? $company : $name) . ' (' . $country . ')';
$subject = '=?UTF-8?B?' . base64_encode($subjectText) . '?=';

$body = "Nouvelle demande de devis depuis rancesales.com ($lang)\n\n"
    . "Nom : $name\n"
    . "Société : $company\n"
    . "Pays : $country\n"
    . "E-mail : $email\n"
    . "Téléphone : $phone\n"
    . "Recontact WhatsApp : $whatsapp\n"
    . "Produit : $product\n"
    . "Volume : $volume\n\n"
    . "Message :\n$message\n";

$headers = [
    'From: Site Rance Sales <no-reply@rancesales.com>',
    'Reply-To: ' . $email,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];

$sent = mail($to, $subject, $body, implode("\r\n", $headers));
header('Location: ' . ($sent ? $thanks : $back . '?erreur=1#devis'));
exit;
