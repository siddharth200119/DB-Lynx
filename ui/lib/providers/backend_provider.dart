import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:dio/dio.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

final backendProvider = FutureProvider<bool>((ref) async {
  await dotenv.load(fileName: ".env");
  final env = dotenv.env['ENV'];

  if (env == 'DEV') {
    try {
      final response = await Dio().get(
        'http://127.0.0.1:42069/api/health-check',
      );
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  } else if (env == 'PROD') {
    // Logic for PROD will be implemented later
    return false;
  }

  return false;
});
