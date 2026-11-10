#include <DHTesp.h>

// Pinos do FarmTech
const int PINO_DHT = 15;
const int PINO_LDR = 34;
const int PINO_RELE = 23;
const int PINO_N = 18;
const int PINO_P = 19;
const int PINO_K = 21;

DHTesp dht;

void setup() {
  Serial.begin(115200);

  dht.setup(PINO_DHT, DHTesp::DHT22);
  pinMode(PINO_RELE, OUTPUT);
  digitalWrite(PINO_RELE, HIGH);
  pinMode(PINO_N, INPUT_PULLUP);
  pinMode(PINO_P, INPUT_PULLUP);
  pinMode(PINO_K, INPUT_PULLUP);

  Serial.println("FarmTech Solutions");
  Serial.println("Monitoramento de Solo e NPK");
}

void loop() {

  int luminosidade = analogRead(PINO_LDR);
  // Conversao do LDR para pH simulado
float phSolo = luminosidade * 14.0 / 4095.0;
  TempAndHumidity dados = dht.getTempAndHumidity();

  // Controle automatico da irrigacao
if (isnan(dados.humidity)) {
  digitalWrite(PINO_RELE, HIGH);
  Serial.println("ERRO: Irrigacao desligada!");
} else if (dados.humidity < 50.0) {
  digitalWrite(PINO_RELE, LOW);
  Serial.println("IRRIGACAO LIGADA - Solo seco!");
} else {
  digitalWrite(PINO_RELE, HIGH);
  Serial.println("IRRIGACAO DESLIGADA - Umidade adequada!");
}

  Serial.println("----- FARMTECH -----");
Serial.print("Luminosidade (LDR): ");
Serial.println(luminosidade);
Serial.print("pH simulado do solo: ");
Serial.println(phSolo, 2);
  if (isnan(dados.humidity) || isnan(dados.temperature)) {
    Serial.println("Erro na leitura do DHT22!");
  } else {
    Serial.print("Umidade simulada do solo: ");
    Serial.print(dados.humidity);
    Serial.println("%");

    Serial.print("Temperatura: ");
    Serial.print(dados.temperature);
    Serial.println(" C");
  }

  Serial.print("Nitrogenio (N): ");
  Serial.println(digitalRead(PINO_N) == LOW ? "Presente" : "Ausente");

  Serial.print("Fosforo (P): ");
  Serial.println(digitalRead(PINO_P) == LOW ? "Presente" : "Ausente");

  Serial.print("Potassio (K): ");
  Serial.println(digitalRead(PINO_K) == LOW ? "Presente" : "Ausente");

  Serial.println("--------------------");

  delay(2000);
}
