# Generated by Django 3.2.5 on 2021-07-17 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atendimento', models.DateField(blank=True, null=True, verbose_name='Data do atendimento')),
                ('num_GTO', models.CharField(blank=True, max_length=30, null=True, verbose_name='Número da GTO')),
                ('data_envio', models.DateField(blank=True, null=True, verbose_name='Data de envio')),
                ('mes_recebimento', models.DateField(blank=True, null=True, verbose_name='Mês de recebimento')),
                ('comentarios', models.CharField(blank=True, max_length=500, verbose_name='Comentários')),
                ('encaminhado_por', models.CharField(blank=True, help_text='Registrar nome do dentista ou funcionário que encaminhou o paciente', max_length=30, verbose_name='Encaminhado por')),
                ('verificado', models.BooleanField(blank=True, default=False, help_text='Atendimento verificado pela administração do consultório', verbose_name='Atendimento verificado')),
            ],
            options={
                'ordering': ['-data_atendimento'],
            },
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convenio', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['convenio'],
            },
        ),
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('num_CRO', models.CharField(blank=True, max_length=100, verbose_name='Número do CRO')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('banco', models.CharField(blank=True, max_length=30)),
                ('num_agencia', models.CharField(blank=True, max_length=4, verbose_name='Agência número')),
                ('num_conta', models.CharField(blank=True, max_length=20, verbose_name='Conta número')),
            ],
            options={
                'ordering': ['nome_completo'],
            },
        ),
        migrations.CreateModel(
            name='Formas_pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pagamento', models.CharField(max_length=30, verbose_name='Forma de pagamento')),
                ('comissao', models.FloatField(blank=True, help_text='Registre aqui o valor da comissão dos meios de pagamento ou da alíquota de impostos', null=True, verbose_name='Comissão/ impostos (%)')),
                ('taxa_fixa', models.FloatField(blank=True, null=True, verbose_name='Taxa Fixa (R$)')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('nome_responsavel', models.CharField(blank=True, max_length=100, verbose_name='Nome do responsável')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
            ],
            options={
                'ordering': ['nome_completo'],
            },
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedimento', models.CharField(max_length=100)),
                ('tabela_preço', models.FloatField(blank=True, null=True, verbose_name='Tabela de preço')),
            ],
            options={
                'ordering': ['procedimento'],
            },
        ),
        migrations.CreateModel(
            name='Tipos_procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_procedimento', models.CharField(blank=True, max_length=30, verbose_name='Tipo do procedimento')),
            ],
        ),
        migrations.CreateModel(
            name='Tabela_preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField(blank=True, null=True, verbose_name='Preço')),
                ('convenio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.convenio')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.procedimento')),
            ],
            options={
                'ordering': ['procedimento'],
            },
        ),
        migrations.CreateModel(
            name='Procedimentos_aplicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dente', models.CharField(blank=True, help_text='Registre qual o dente tratado', max_length=20)),
                ('descr_anterior', models.CharField(blank=True, help_text='Descrição anterior do procedimento (Opcional)', max_length=200, verbose_name='Descrição do procedimento')),
                ('valor_real', models.FloatField(blank=True, null=True, verbose_name='Valor')),
                ('valor_liquido_recebido', models.FloatField(blank=True, null=True, verbose_name='Valor líquido efetivamente recebido')),
                ('valor_repassado', models.FloatField(blank=True, null=True, verbose_name='Valor repassado ao dentista')),
                ('recebido', models.BooleanField(blank=True, default=False)),
                ('glosado', models.BooleanField(blank=True, default=False)),
                ('motivo_glosa', models.CharField(blank=True, max_length=200, verbose_name='Motivo da glosa')),
                ('data_recebimento', models.DateField(blank=True, null=True, verbose_name='Data de recebimento')),
                ('data_repasse', models.DateField(blank=True, null=True, verbose_name='Data de repasse')),
                ('repassado', models.BooleanField(blank=True, default=False)),
                ('atendimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alisystem.atendimento')),
                ('procedimento', models.ForeignKey(blank=True, help_text='Escolha o seu procedimento nesta lista, ou insira um novo procedimento clicando no sinal de +', null=True, on_delete=django.db.models.deletion.CASCADE, to='Alisystem.procedimento')),
            ],
        ),
        migrations.AddField(
            model_name='procedimento',
            name='tipo_procedimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alisystem.tipos_procedimento', verbose_name='Tipo do procedimento'),
        ),
        migrations.CreateModel(
            name='Encaminhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('data_encaminhamento', models.DateField(verbose_name='Data do encaminhamento')),
                ('dentista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.dentista')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.paciente')),
            ],
            options={
                'ordering': ['paciente'],
            },
        ),
        migrations.AddField(
            model_name='atendimento',
            name='convenio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alisystem.convenio'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='dentista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.dentista'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='forma_pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alisystem.formas_pagamento', verbose_name='Forma de pagamento'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alisystem.paciente'),
        ),
    ]
