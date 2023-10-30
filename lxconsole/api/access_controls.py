from flask import jsonify, request, session
import json
import requests
from lxconsole import db, bcrypt
from lxconsole.models import AccessControl, Server, Group, UserGroup
from flask_login import login_required, current_user


def privilege_check(privilege, server_id = 0):
  privileges = {
    'Auditor' : [
      #'add_access_control',
      #'add_certificate',
      #'add_cluster_group',
      #'add_cluster_member',
      #'add_group',
      #'add_server',
      #'add_image',
      #'add_instance_disk_device',
      #'add_instance_gpu_device',
      #'add_instance_network_device',
      #'add_instance_proxy_device',
      #'add_instance_unix_device',
      #'add_instance_usb_device',
      #'add_instance',
      #'add_network_acl',
      #'add_network_zone',
      #'add_network_load_balancer',
      #'add_network_forward',
      #'add_network_peer',
      #'add_network',
      #'add_profile',
      #'add_project',
      #'add_role',
      #'add_simplestream',
      #'add_storage_pool',
      #'add_storage_volume',
      #'add_user',
      #'attach_instance_profile',
      #'change_cluster_member_state',
      #'change_instance_state',
      #'copy_instance',
      'copy_instance_proc_meminfo',
      'copy_instance_proc_stat',
      #'create_instance_backup',
      #'create_instance_snapshot_instance',
      #'create_instance_snapshot',
      #'delete_access_control',
      #'delete_certificate',
      #'delete_cluster_group',
      #'delete_cluster_member',
      #'delete_group',
      #'delete_image',
      #'delete_instance_backup',
      #'delete_instance_device',
      #'delete_instance_log',
      #'delete_instance_snapshot',
      #'delete_instance',
      #'delete_instance',
      #'delete_network_acl',
      #'delete_network_zone',
      #'delete_network_load_balancer',
      #'delete_network_forward',
      #'delete_network_peer',
      #'delete_network',
      #'delete_operation',
      #'delete_profile',
      #'delete_project',
      #'delete_role',
      #'delete_simplestream',
      #'delete_storage_pool',
      #'delete_storage_volume',
      #'delete_user',
      #'detach_instance_profile',
      'display_instance_log',
      #'establish_instance_console_websocket',
      #'establish_instance_exec_websocket',
      #'export_instance_backup',
      'get_access_control',
      'get_group',
      'get_network_state',
      'get_server_info',
      'get_server_initial_project',
      'get_server_resources',
      'get_server_warnings',
      'get_server',
      'get_instance_cpu_usage',
      'get_instance_disk_devices',
      'get_instance_gpu_devices',
      'get_instance_interfaces',
      'get_instance_network_devices',
      'get_instance_proc_meminfo',
      'get_instance_proc_stat',
      'get_instance_proxy_devices',
      'get_instance_state',
      'get_instance_unix_devices',
      'get_instance_usb_devices',
      'get_instance_websocket_host',
      'get_instance',
      'get_role',
      'get_user',
      'is_cluster_member_enabled',
      'list_access_controls',
      'list_certificates',
      'list_cluster_groups',
      'list_cluster_members',
      'list_groups',
      'list_servers',
      'list_images',
      'list_instance_backups',
      'list_instance_logs',
      'list_instance_snapshots',
      'list_instances',
      'list_logs',
      'list_network_acls',
      'list_network_forwards',
      'list_network_leases',
      'list_network_load_balancers',
      'list_network_peers',
      'list_network_zones',
      'list_network_managed_devices',
      'list_networks',
      'list_operations',
      'list_profiles',
      'list_projects',
      'list_roles',
      'list_simplestream_images',
      'list_simplestreams',
      'list_storage_pools',
      'list_storage_volumes',
      'list_users',
      'load_certificate',
      'load_cluster_group',
      'load_cluster_member',
      'load_image',
      'load_instance',
      'load_network_acl',
      'load_network_forward',
      'load_network_lease',
      'load_network_load_balancer',
      'load_network_peer',
      'load_network_zone',
      'load_network',
      'load_operation',
      'load_profile',
      'load_project',
      'load_storage_pool',
      'load_storage_volume',
      #'migrate_instance',
      #'publish_instance_snapshot',
      #'publish_instance',
      #'refresh_image',
      #'remove_server',
      #'rename_instance',
      #'restore_instance_snapshot',
      #'update_access_control',
      #'update_certificate',
      #'update_cluster_group',
      #'update_cluster_member',
      #'update_group',
      #'update_server',
      #'update_image',
      #'update_instance',
      #'update_network_acl',
      #'update_network_forward',
      #'update_network_lease',
      #'update_network_load_balancer',
      #'update_network_peer',
      #'update_network_zone',
      #'update_network',
      #'update_profile',
      #'update_project',
      #'update_role',
      #'update_simplestream',
      #'update_storage_pool',
      #'update_storage_volume',
      #'update_user',  
    ],
    'User': [
      #'add_access_control',
      #'add_certificate',
      #'add_cluster_group',
      #'add_cluster_member',
      #'add_group',
      #'add_server',
      #'add_image',
      #'add_instance_disk_device',
      #'add_instance_gpu_device',
      #'add_instance_network_device',
      #'add_instance_proxy_device',
      #'add_instance_unix_device',
      #'add_instance_usb_device',
      #'add_instance',
      #'add_network_acl',
      #'add_network_zone',
      #'add_network_load_balancer',
      #'add_network_forward',
      #'add_network_peer',
      #'add_network',
      #'add_profile',
      #'add_project',
      #'add_role',
      #'add_simplestream',
      #'add_storage_pool',
      #'add_storage_volume',
      #'add_user',
      #'attach_instance_profile',
      'change_cluster_member_state',
      'change_instance_state',
      'copy_instance',
      'copy_instance_proc_meminfo',
      'copy_instance_proc_stat',
      'create_instance_backup',
      'create_instance_snapshot_instance',
      'create_instance_snapshot',
      #'delete_access_control',
      #'delete_certificate',
      #'delete_cluster_group',
      #'delete_cluster_member',
      #'delete_group',
      #'delete_image',
      #'delete_instance_backup',
      #'delete_instance_device',
      #'delete_instance_log',
      #'delete_instance_snapshot',
      #'delete_instance',
      #'delete_instance',
      #'delete_network_acl',
      #'delete_network_zone',
      #'delete_network_load_balancer',
      #'delete_network_forward',
      #'delete_network_peer',
      #'delete_network',
      #'delete_operation',
      #'delete_profile',
      #'delete_project',
      #'delete_role',
      #'delete_simplestream',
      #'delete_storage_pool',
      #'delete_storage_volume',
      #'delete_user',
      #'detach_instance_profile',
      'display_instance_log',
      'establish_instance_console_websocket',
      'establish_instance_exec_websocket',
      'export_instance_backup',
      'get_access_control',
      'get_group',
      'get_network_state',
      'get_server_info',
      'get_server_initial_project',
      'get_server_resources',
      'get_server_warnings',
      'get_server',
      'get_instance_cpu_usage',
      'get_instance_disk_devices',
      'get_instance_gpu_devices',
      'get_instance_interfaces',
      'get_instance_network_devices',
      'get_instance_proc_meminfo',
      'get_instance_proc_stat',
      'get_instance_proxy_devices',
      'get_instance_state',
      'get_instance_unix_devices',
      'get_instance_usb_devices',
      'get_instance_websocket_host',
      'get_instance',
      'get_role',
      'get_user',
      'is_cluster_member_enabled',
      'list_access_controls',
      'list_certificates',
      'list_cluster_groups',
      'list_cluster_members',
      'list_groups',
      'list_servers',
      'list_images',
      'list_instance_backups',
      'list_instance_logs',
      'list_instance_snapshots',
      'list_instances',
      'list_logs',
      'list_network_acls',
      'list_network_forwards',
      'list_network_leases',
      'list_network_load_balancers',
      'list_network_peers',
      'list_network_zones',
      'list_network_managed_devices',
      'list_networks',
      'list_operations',
      'list_profiles',
      'list_projects',
      'list_roles',
      'list_simplestream_images',
      'list_simplestreams',
      'list_storage_pools',
      'list_storage_volumes',
      'list_users',
      'load_certificate',
      'load_cluster_group',
      'load_cluster_member',
      'load_image',
      'load_instance',
      'load_network_acl',
      'load_network_forward',
      'load_network_lease',
      'load_network_load_balancer',
      'load_network_peer',
      'load_network_zone',
      'load_network',
      'load_operation',
      'load_profile',
      'load_project',
      'load_storage_pool',
      'load_storage_volume',
      'migrate_instance',
      'publish_instance_snapshot',
      'publish_instance',
      #'refresh_image',
      #'remove_server',
      #'rename_instance',
      'restore_instance_snapshot',
      #'update_access_control',
      #'update_certificate',
      #'update_cluster_group',
      #'update_cluster_member',
      #'update_group',
      #'update_server',
      #'update_image',
      #'update_instance',
      #'update_network_acl',
      #'update_network_forward',
      #'update_network_lease',
      #'update_network_load_balancer',
      #'update_network_peer',
      #'update_network_zone',
      #'update_network',
      #'update_profile',
      #'update_project',
      #'update_role',
      #'update_simplestream',
      #'update_storage_pool',
      #'update_storage_volume',
      #'update_user',  
    ],
    'Operator': [
      #'add_access_control',
      'add_certificate',
      'add_cluster_group',
      'add_cluster_member',
      #'add_group',
      'add_server',
      'add_image',
      'add_instance_disk_device',
      'add_instance_gpu_device',
      'add_instance_network_device',
      'add_instance_proxy_device',
      'add_instance_unix_device',
      'add_instance_usb_device',
      'add_instance',
      'add_network_acl',
      'add_network_zone',
      'add_network_load_balancer',
      'add_network_forward',
      'add_network_peer',
      'add_network',
      'add_profile',
      'add_project',
      #'add_role',
      'add_simplestream',
      'add_storage_pool',
      'add_storage_volume',
      #'add_user',
      'attach_instance_profile',
      'change_cluster_member_state',
      'change_instance_state',
      'copy_instance',
      'copy_instance_proc_meminfo',
      'copy_instance_proc_stat',
      'create_instance_backup',
      'create_instance_snapshot_instance',
      'create_instance_snapshot',
      #'delete_access_control',
      'delete_certificate',
      'delete_cluster_group',
      'delete_cluster_member',
      #'delete_group',
      #'delete_image',
      'delete_instance_backup',
      'delete_instance_device',
      'delete_instance_log',
      'delete_instance_snapshot',
      'delete_instance',
      'delete_instance',
      'delete_network_acl',
      'delete_network_zone',
      'delete_network_load_balancer',
      'delete_network_forward',
      'delete_network_peer',
      'delete_network',
      'delete_operation',
      'delete_profile',
      'delete_project',
      'delete_role',
      'delete_simplestream',
      'delete_storage_pool',
      'delete_storage_volume',
      #'delete_user',
      'detach_instance_profile',
      'display_instance_log',
      'establish_instance_console_websocket',
      'establish_instance_exec_websocket',
      'export_instance_backup',
      'get_access_control',
      'get_group',
      'get_network_state',
      'get_server_info',
      'get_server_initial_project',
      'get_server_resources',
      'get_server_warnings',
      'get_server',
      'get_instance_cpu_usage',
      'get_instance_disk_devices',
      'get_instance_gpu_devices',
      'get_instance_interfaces',
      'get_instance_network_devices',
      'get_instance_proc_meminfo',
      'get_instance_proc_stat',
      'get_instance_proxy_devices',
      'get_instance_state',
      'get_instance_unix_devices',
      'get_instance_usb_devices',
      'get_instance_websocket_host',
      'get_instance',
      'get_role',
      'get_user',
      'is_cluster_member_enabled',
      'list_access_controls',
      'list_certificates',
      'list_cluster_groups',
      'list_cluster_members',
      'list_groups',
      'list_servers',
      'list_images',
      'list_instance_backups',
      'list_instance_logs',
      'list_instance_snapshots',
      'list_instances',
      'list_logs',
      'list_network_acls',
      'list_network_forwards',
      'list_network_leases',
      'list_network_load_balancers',
      'list_network_peers',
      'list_network_zones',
      'list_network_managed_devices',
      'list_networks',
      'list_operations',
      'list_profiles',
      'list_projects',
      'list_roles',
      'list_simplestream_images',
      'list_simplestreams',
      'list_storage_pools',
      'list_storage_volumes',
      'list_users',
      'load_certificate',
      'load_cluster_group',
      'load_cluster_member',
      'load_image',
      'load_instance',
      'load_network_acl',
      'load_network_forward',
      'load_network_lease',
      'load_network_load_balancer',
      'load_network_peer',
      'load_network_zone',
      'load_network',
      'load_operation',
      'load_profile',
      'load_project',
      'load_storage_pool',
      'load_storage_volume',
      'migrate_instance',
      'publish_instance_snapshot',
      'publish_instance',
      'refresh_image',
      'remove_server',
      'rename_instance',
      'restore_instance_snapshot',
      #'update_access_control',
      'update_certificate',
      'update_cluster_group',
      'update_cluster_member',
      #'update_group',
      'update_server',
      'update_image',
      'update_instance',
      'update_network_acl',
      'update_network_forward',
      'update_network_lease',
      'update_network_load_balancer',
      'update_network_peer',
      'update_network_zone',
      'update_network',
      'update_profile',
      'update_project',
      #'update_role',
      'update_simplestream',
      'update_storage_pool',
      'update_storage_volume',
      #'update_user', 
    ],
    'Administrator': [
      'add_access_control',
      'add_certificate',
      'add_cluster_group',
      'add_cluster_member',
      'add_group',
      'add_server',
      'add_image',
      'add_instance_disk_device',
      'add_instance_gpu_device',
      'add_instance_network_device',
      'add_instance_proxy_device',
      'add_instance_unix_device',
      'add_instance_usb_device',
      'add_instance',
      'add_network_acl',
      'add_network_zone',
      'add_network_load_balancer',
      'add_network_forward',
      'add_network_peer',
      'add_network',
      'add_profile',
      'add_project',
      'add_role',
      'add_simplestream',
      'add_storage_pool',
      'add_storage_volume',
      'add_user',
      'attach_instance_profile',
      'change_cluster_member_state',
      'change_instance_state',
      'copy_instance',
      'copy_instance_proc_meminfo',
      'copy_instance_proc_stat',
      'create_instance_backup',
      'create_instance_snapshot_instance',
      'create_instance_snapshot',
      'delete_access_control',
      'delete_certificate',
      'delete_cluster_group',
      'delete_cluster_member',
      'delete_group',
      'delete_image',
      'delete_instance_backup',
      'delete_instance_device',
      'delete_instance_log',
      'delete_instance_snapshot',
      'delete_instance',
      'delete_instance',
      'delete_network_acl',
      'delete_network_zone',
      'delete_network_load_balancer',
      'delete_network_forward',
      'delete_network_peer',
      'delete_network',
      'delete_operation',
      'delete_profile',
      'delete_project',
      'delete_role',
      'delete_simplestream',
      'delete_storage_pool',
      'delete_storage_volume',
      'delete_user',
      'detach_instance_profile',
      'display_instance_log',
      'establish_instance_console_websocket',
      'establish_instance_exec_websocket',
      'export_instance_backup',
      'get_access_control',
      'get_group',
      'get_network_state',
      'get_server_info',
      'get_server_initial_project',
      'get_server_resources',
      'get_server_warnings',
      'get_server',
      'get_instance_cpu_usage',
      'get_instance_disk_devices',
      'get_instance_gpu_devices',
      'get_instance_interfaces',
      'get_instance_network_devices',
      'get_instance_proc_meminfo',
      'get_instance_proc_stat',
      'get_instance_proxy_devices',
      'get_instance_state',
      'get_instance_unix_devices',
      'get_instance_usb_devices',
      'get_instance_websocket_host',
      'get_instance',
      'get_role',
      'get_user',
      'is_cluster_member_enabled',
      'list_access_controls',
      'list_certificates',
      'list_cluster_groups',
      'list_cluster_members',
      'list_groups',
      'list_servers',
      'list_images',
      'list_instance_backups',
      'list_instance_logs',
      'list_instance_snapshots',
      'list_instances',
      'list_logs',
      'list_network_acls',
      'list_network_forwards',
      'list_network_leases',
      'list_network_load_balancers',
      'list_network_peers',
      'list_network_zones',
      'list_network_managed_devices',
      'list_networks',
      'list_operations',
      'list_profiles',
      'list_projects',
      'list_roles',
      'list_simplestream_images',
      'list_simplestreams',
      'list_storage_pools',
      'list_storage_volumes',
      'list_users',
      'load_certificate',
      'load_cluster_group',
      'load_cluster_member',
      'load_image',
      'load_instance',
      'load_network_acl',
      'load_network_forward',
      'load_network_lease',
      'load_network_load_balancer',
      'load_network_peer',
      'load_network_zone',
      'load_network',
      'load_operation',
      'load_profile',
      'load_project',
      'load_storage_pool',
      'load_storage_volume',
      'migrate_instance',
      'publish_instance_snapshot',
      'publish_instance',
      'refresh_image',
      'remove_server',
      'rename_instance',
      'restore_instance_snapshot',
      'update_access_control',
      'update_certificate',
      'update_cluster_group',
      'update_cluster_member',
      'update_group',
      'update_server',
      'update_image',
      'update_instance',
      'update_network_acl',
      'update_network_forward',
      'update_network_lease',
      'update_network_load_balancer',
      'update_network_peer',
      'update_network_zone',
      'update_network',
      'update_profile',
      'update_project',
      'update_role',
      'update_simplestream',
      'update_storage_pool',
      'update_storage_volume',
      'update_user',      
      ]
    }
  for global_role in session['global_roles']:
    if privilege in privileges[global_role]:
      return True
  # if session['host_roles'][server_id]:
  #   for server_role in session['host_roles'][server_id]:
  #     if privilege in privileges[host_role]:
  #       return True
  return False


@login_required
def api_access_controls_endpoint(endpoint):

  if endpoint == 'add_access_control':
    scope = request.form.get('scope')
    description = request.form.get('description')
    group_id = request.form.get('group_id')
    server_id = request.form.get('server_id')
    role_id = request.form.get('role_id')
    if not scope or not group_id or not role_id:
      return jsonify({'error': 'missing required data'})
    access_control = AccessControl(scope=scope, description=description, group_id=group_id, server_id=server_id, role_id=role_id)
    db.session.add(access_control)
    db.session.commit()
    json_object = json.loads('{"status": 200}')
    return jsonify(json_object)


  if endpoint == 'get_access_control':
    id = request.args.get('id')
    access_control = AccessControl.query.filter_by(id=id).first()
    data = {}
    data.update({'id': access_control.id})
    data.update({'scope': access_control.scope})
    data.update({'description': access_control.description})
    data.update({'group_id': access_control.group_id})
    data.update({'role_id': access_control.role_id})
    return jsonify({"metadata": data})
  
  
  if endpoint == 'delete_access_control':
    id = request.form.get('id')
    access_control = AccessControl.query.filter_by(id=id).first()
    db.session.delete(access_control)
    db.session.commit()
    json_object = json.loads('{"status": 200}')
    return jsonify(json_object)


  if endpoint == 'list_access_controls':
    access_controls = AccessControl.query.all()
    acls = []
    for access_control in access_controls:
      group = Group.query.filter_by(id=access_control.group_id).first()
      #server = Server.query.filter_by(id=access_control.server_id).first()
      
      role_id = ""
      role_name = ""
      for role in session['roles']:
        if role['id'] == access_control.role_id:
          role_id = role['id']
          role_name = role['name']

      data = {}
      data.update({ "id": access_control.id })
      data.update({ "scope": access_control.scope })
      data.update({ "description": access_control.description })
      data.update({ "group_id": group.id })
      data.update({ "role_id": role_id })
      # Display names to make more user friendly
      data.update({ "group_name": group.name })
      data.update({ "role_name": role_name })
      acls.append(data)
    return jsonify({"data": acls})


  if endpoint == 'update_access_control':
    id = request.form.get('id')
    access_control = AccessControl.query.filter_by(id=id).first()
    access_control.scope = request.form.get('scope')
    access_control.description = request.form.get('description')
    access_control.group_id = request.form.get('group_id')
    access_control.role_id = request.form.get('role_id')
    if not access_control.scope or not access_control.group_id or not access_control.role_id:
      return jsonify({'error': 'missing required data'})
    db.session.commit()
    return jsonify({"alert": "Access control updated"})
