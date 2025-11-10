import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:ui/providers/backend_provider.dart';

class LoadingScreen extends ConsumerWidget {
  const LoadingScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;
    final backendStatus = ref.watch(backendProvider);

    return Scaffold(
      body: Center(
        child: backendStatus.when(
          loading: () => Text(
            'loading...',
            style: TextStyle(color: colorScheme.primary, fontSize: 50),
          ),
          data: (isConnected) {
            if (isConnected) {
              return Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    'Connected to backend!',
                    style: TextStyle(color: colorScheme.primary, fontSize: 30),
                  ),
                  const SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      // Navigate to the next screen
                    },
                    child: const Text('Continue'),
                  ),
                ],
              );
            } else {
              return Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    'Failed to connect to backend',
                    style: TextStyle(color: colorScheme.error, fontSize: 30),
                  ),
                  const SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      ref.refresh(backendProvider);
                    },
                    child: const Text('Retry'),
                  ),
                ],
              );
            }
          },
          error: (err, stack) => Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'An error occurred',
                style: TextStyle(color: colorScheme.error, fontSize: 30),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  ref.refresh(backendProvider);
                },
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

