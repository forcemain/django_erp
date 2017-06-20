# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 13:16
from __future__ import unicode_literals

import common.fields
import common.state
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangoperm.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('is_virtual', djangoperm.db.fields.BooleanField(default=False, help_text='库位的虚拟状态', perms={'read': False, 'write': False}, verbose_name='虚拟库位')),
                ('x', djangoperm.db.fields.CharField(blank=True, help_text='库位的X轴坐标', max_length=90, perms={'read': False, 'write': False}, verbose_name='X')),
                ('y', djangoperm.db.fields.CharField(blank=True, help_text='库位的Y轴坐标', max_length=90, perms={'read': False, 'write': False}, verbose_name='Y')),
                ('z', djangoperm.db.fields.CharField(blank=True, help_text='库位的Z轴坐标', max_length=90, perms={'read': False, 'write': False}, verbose_name='Z')),
                ('parent_location', common.fields.ActiveLimitForeignKey(blank=True, help_text='库位所属的上级库位,若库位为区域的基本库位,则必须为虚拟库位', null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.Location', verbose_name='上级库位')),
            ],
            options={
                'verbose_name': '库位',
                'verbose_name_plural': '库位',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('quantity', common.fields.QuantityField(decimal_places=12, help_text='产品的数量', max_digits=24, perms={'read': False, 'write': False}, uom='product.uom', verbose_name='移动数量')),
                ('end_location', common.fields.ActiveLimitForeignKey(help_text='移动链的最终的库位', on_delete=django.db.models.deletion.PROTECT, related_name='converge_moves', to='stock.Location', verbose_name='最终库位')),
                ('from_location', common.fields.ActiveLimitForeignKey(help_text='移动的起始库位', on_delete=django.db.models.deletion.PROTECT, related_name='out_moves', to='stock.Location', verbose_name='起始库位')),
                ('initial_location', common.fields.ActiveLimitForeignKey(help_text='移动链的最初的库位', on_delete=django.db.models.deletion.PROTECT, related_name='spread_moves', to='stock.Location', verbose_name='初始库位')),
            ],
            options={
                'verbose_name': ('移动',),
                'verbose_name_plural': '移动',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('context', djangoperm.db.fields.TextField(help_text='包裹的附加说明', perms={'read': False, 'write': False}, verbose_name='说明')),
            ],
            options={
                'verbose_name': ('包裹',),
                'verbose_name_plural': '包裹',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='PackageNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', djangoperm.db.fields.CharField(help_text='打包方法的名称', max_length=90, perms={'read': False, 'write': False}, unique=True, verbose_name='名称')),
                ('quantity', djangoperm.db.fields.PositiveSmallIntegerField(default=1, help_text='包裹的数量', perms={'read': False, 'write': False}, verbose_name='数量')),
                ('index', djangoperm.db.fields.CharField(blank=True, default='', help_text='该包裹所在包裹树的索引', max_length=190, perms={'read': False, 'write': False}, verbose_name='索引')),
                ('level', djangoperm.db.fields.PositiveSmallIntegerField(default=0, help_text='该包裹所距离所在包裹树的根的距离', perms={'read': False, 'write': False}, verbose_name='树层')),
                ('parent_node', common.fields.ActiveLimitForeignKey(default=None, help_text='包裹该节点的节点', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_nodes', to='stock.PackageNode', verbose_name='父节点')),
            ],
            options={
                'verbose_name': '包裹节点',
                'verbose_name_plural': '包裹节点',
            },
        ),
        migrations.CreateModel(
            name='PackageTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '包裹模板',
                'verbose_name_plural': '包裹模板',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='PackageTemplateProductSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', common.fields.QuantityField(decimal_places=12, help_text='包裹模板包含该产品的数量', max_digits=24, perms={'read': False, 'write': False}, uom='product.uom', verbose_name='最大数量')),
                ('package_template', common.fields.ActiveLimitForeignKey(help_text='相关的包裹模板', on_delete=django.db.models.deletion.PROTECT, related_name='package_template_settings', to='stock.PackageTemplate', verbose_name='包裹模板')),
                ('product', common.fields.ActiveLimitForeignKey(help_text='相关的产品', on_delete=django.db.models.deletion.PROTECT, related_name='package_template_settings', to='product.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '包裹模板产品设置',
                'verbose_name_plural': '包裹模板产品设置',
            },
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('name', djangoperm.db.fields.CharField(help_text='包裹类型的名称', max_length=90, perms={'read': False, 'write': False}, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '包裹类型',
                'verbose_name_plural': '包裹类型',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='PackageTypeProductSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_quantity', common.fields.QuantityField(decimal_places=12, help_text='包裹类型能够包含该产品的最大数量', max_digits=24, perms={'read': False, 'write': False}, uom='product.uom', verbose_name='最大数量')),
                ('package_type', common.fields.ActiveLimitForeignKey(help_text='相关的包裹类型', on_delete=django.db.models.deletion.PROTECT, related_name='package_type_settings', to='stock.PackageType', verbose_name='包裹类型')),
                ('product', common.fields.ActiveLimitForeignKey(help_text='相关的产品', on_delete=django.db.models.deletion.PROTECT, related_name='package_type_settings', to='product.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '包裹类型产品设置',
                'verbose_name_plural': '包裹类型产品设置',
            },
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('from_location', common.fields.ActiveLimitForeignKey(help_text='产品从该库位移出', on_delete=django.db.models.deletion.PROTECT, related_name='out_paths', to='stock.Location', verbose_name='源库位')),
                ('to_location', common.fields.ActiveLimitForeignKey(help_text='产品向该库位移入', on_delete=django.db.models.deletion.PROTECT, related_name='in_paths', to='stock.Location', verbose_name='目标库位')),
            ],
            options={
                'verbose_name': '路径',
                'verbose_name_plural': '路径',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('to_location', common.fields.ActiveLimitForeignKey(help_text='需求产生的库位', on_delete=django.db.models.deletion.PROTECT, to='stock.Location', verbose_name='库位')),
                ('user', common.fields.PartnerForeignKey(help_text='提出需求的相关合作伙伴', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='合作伙伴')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='ProcurementDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '需求明细',
                'verbose_name_plural': '需求明细',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='ProcurementFromLocationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', common.fields.QuantityField(decimal_places=12, help_text='产品的数量', max_digits=24, perms={'read': False, 'write': False}, uom='product.uom', verbose_name='移动数量')),
                ('detail', common.fields.ActiveLimitForeignKey(help_text='相关的需求', on_delete=django.db.models.deletion.PROTECT, related_name='procurement_from_location_settings', to='stock.ProcurementDetail', verbose_name='需求明细')),
                ('location', common.fields.ActiveLimitForeignKey(help_text='相关的位置', on_delete=django.db.models.deletion.PROTECT, related_name='procurement_from_location_settings', to='stock.Location', verbose_name='来源位置')),
            ],
            options={
                'verbose_name': '需求产品来源设置',
                'verbose_name_plural': '需求产品来源设置',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('name', djangoperm.db.fields.CharField(help_text='路线的名称', max_length=190, perms={'read': False, 'write': False}, verbose_name='名称')),
                ('map', djangoperm.db.fields.ShortJSONField(help_text='以json格式保存的路径顺序', json_type='list', max_length=190, perms={'read': False, 'write': False}, unique=True)),
                ('return_method', djangoperm.db.fields.CharField(choices=[('direct', '直接退货'), ('fallback', '回滚退货'), ('config', '自定义退货')], default='direct', help_text='路线的退货方法', max_length=10, perms={'read': False, 'write': False}, verbose_name='退货方法')),
                ('sequence', djangoperm.db.fields.PositiveSmallIntegerField(default=0, help_text='在相同起始库位和终点库位的路线的优先级', perms={'read': False, 'write': False}, verbose_name='优先级')),
                ('direct_path', common.fields.ActiveLimitForeignKey(help_text='表示路线起始库位到最终库位的路径', on_delete=django.db.models.deletion.PROTECT, related_name='direct_routes', to='stock.Path', verbose_name='直线路径')),
                ('paths', models.ManyToManyField(help_text='路线的详细路径', to='stock.Path', verbose_name='路径')),
                ('return_route', common.fields.ActiveLimitForeignKey(blank=True, help_text='路线的自定义退货路线', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='origin_routes', to='stock.Route', verbose_name='自定义退货路线')),
            ],
            options={
                'verbose_name': '路线',
                'verbose_name_plural': '路线',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('name', djangoperm.db.fields.CharField(help_text='仓库的名称', max_length=90, perms={'read': False, 'write': False}, verbose_name='名称')),
                ('is_inside', djangoperm.db.fields.BooleanField(default=True, help_text='是否为内部仓库', perms={'read': False, 'write': False}, verbose_name='是否为内部仓库')),
                ('address', common.fields.ActiveLimitForeignKey(help_text='仓库的地理位置', on_delete=django.db.models.deletion.PROTECT, to='account.Address', verbose_name='地址')),
                ('user', common.fields.PartnerForeignKey(help_text='仓库的相关合作伙伴或联系人', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='联系人')),
            ],
            options={
                'verbose_name': '仓库',
                'verbose_name_plural': '仓库',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', djangoperm.db.fields.BooleanField(default=True, help_text='记录的可用状态,False为不可用,True为可用', perms={'read': False, 'write': False}, verbose_name='可用状态')),
                ('is_delete', djangoperm.db.fields.BooleanField(default=False, help_text='记录的删除状态,True删除不可视,False为尚未删除', perms={'read': False, 'write': False}, verbose_name='删除状态')),
                ('create_time', djangoperm.db.fields.DateTimeField(auto_now_add=True, help_text='记录的创建时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='创建时间')),
                ('last_modify_time', djangoperm.db.fields.DateTimeField(auto_now=True, help_text='记录的最后修改时间,UTC时间', perms={'read': False, 'write': False}, verbose_name='最后修改时间')),
                ('usage', djangoperm.db.fields.CharField(choices=[('stock', '仓库'), ('transfer-pick', '分拣流程区域'), ('transfer-check', '验货流程区域'), ('transfer-pack', '包裹流程区域'), ('transfer-stream-wait', '物流等待流程区域'), ('transfer-stream-deliver', '物流运输流程区域'), ('customer', '顾客区域'), ('supplier', '供应商区域'), ('produce', '生产区域'), ('repair', '返工维修区域'), ('scrap', '报废区域'), ('close-out', '平仓区域'), ('initial', '初始区域')], default='container', help_text='区域的用途', max_length=20, perms={'read': False, 'write': False}, verbose_name='用途')),
                ('self_location', common.fields.ActiveLimitOneToOneField(help_text='区域的基本位置', on_delete=django.db.models.deletion.CASCADE, related_name='self_zone', to='stock.Location', verbose_name='库位')),
                ('warehouse', common.fields.ActiveLimitForeignKey(help_text='区域所属的仓库', on_delete=django.db.models.deletion.PROTECT, to='stock.Warehouse', verbose_name='仓库')),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域',
            },
            bases=(models.Model, common.state.StateMachine),
        ),
        migrations.AddField(
            model_name='procurementfromlocationsettings',
            name='route',
            field=common.fields.ActiveLimitForeignKey(help_text='与需求相关的路线', on_delete=django.db.models.deletion.PROTECT, to='stock.Route', verbose_name='路线'),
        ),
        migrations.AddField(
            model_name='procurementdetail',
            name='from_locations',
            field=models.ManyToManyField(help_text='需求产品的来源位置', related_name='procurement_details', through='stock.ProcurementFromLocationSettings', to='stock.Location', verbose_name='来源位置'),
        ),
        migrations.AddField(
            model_name='procurementdetail',
            name='procurement',
            field=common.fields.ActiveLimitForeignKey(help_text='需求明细所属的需求', on_delete=django.db.models.deletion.PROTECT, related_name='procurement_details', to='stock.Procurement', verbose_name='需求'),
        ),
        migrations.AddField(
            model_name='procurementdetail',
            name='product',
            field=common.fields.ActiveLimitForeignKey(help_text='明细相关的产品', on_delete=django.db.models.deletion.PROTECT, to='product.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='packagetype',
            name='products',
            field=models.ManyToManyField(help_text='包裹可包装的产品', related_name='package_types', through='stock.PackageTypeProductSetting', to='product.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='packagetemplate',
            name='package_type',
            field=common.fields.ActiveLimitForeignKey(help_text='包裹模板的类型', on_delete=django.db.models.deletion.PROTECT, to='stock.PackageType', verbose_name='包裹类型'),
        ),
        migrations.AddField(
            model_name='packagetemplate',
            name='products',
            field=models.ManyToManyField(help_text='包裹可包装的产品', related_name='package_templates', through='stock.PackageTemplateProductSetting', to='product.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='packagenode',
            name='template',
            field=common.fields.ActiveLimitForeignKey(help_text='打包方法相关的包裹类型', on_delete=django.db.models.deletion.PROTECT, to='stock.PackageTemplate', verbose_name='包裹类型'),
        ),
        migrations.AddField(
            model_name='package',
            name='root_node',
            field=models.OneToOneField(help_text='包裹树的根节点', on_delete=django.db.models.deletion.CASCADE, to='stock.PackageNode', verbose_name='根节点'),
        ),
        migrations.AddField(
            model_name='move',
            name='procurement_detail_setting',
            field=common.fields.ActiveLimitForeignKey(help_text='生成该移动的需求明细设置', on_delete=django.db.models.deletion.PROTECT, to='stock.ProcurementFromLocationSettings', verbose_name='需求明细设置'),
        ),
        migrations.AddField(
            model_name='move',
            name='product',
            field=common.fields.ActiveLimitForeignKey(help_text='明细相关的产品', on_delete=django.db.models.deletion.PROTECT, to='product.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='move',
            name='to_location',
            field=common.fields.ActiveLimitForeignKey(help_text='移动的结束库位', on_delete=django.db.models.deletion.PROTECT, related_name='in_moves', to='stock.Location', verbose_name='结束库位'),
        ),
        migrations.AddField(
            model_name='move',
            name='to_move',
            field=common.fields.ActiveLimitOneToOneField(blank=True, help_text='计划移动链的后续移动', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_move', to='stock.Move', verbose_name='后续移动'),
        ),
        migrations.AddField(
            model_name='location',
            name='zone',
            field=common.fields.ActiveLimitForeignKey(help_text='库位所属的区域', on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='stock.Zone', verbose_name='区域'),
        ),
        migrations.AlterUniqueTogether(
            name='zone',
            unique_together=set([('warehouse', 'usage')]),
        ),
        migrations.AlterUniqueTogether(
            name='procurementfromlocationsettings',
            unique_together=set([('detail', 'location')]),
        ),
        migrations.AlterUniqueTogether(
            name='path',
            unique_together=set([('from_location', 'to_location')]),
        ),
        migrations.AlterUniqueTogether(
            name='packagetypeproductsetting',
            unique_together=set([('package_type', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='packagetemplateproductsetting',
            unique_together=set([('package_template', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='packagenode',
            unique_together=set([('parent_node', 'template')]),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('zone', 'x', 'y', 'z')]),
        ),
    ]
